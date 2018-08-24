import tweepy as tp
import src.twitter.config
from tweepy.error import TweepError, RateLimitError
import time
import datetime

auth = tp.OAuthHandler(src.twitter.config.consumer_key, src.twitter.config.consumer_secret)
auth.set_access_token(src.twitter.config.access_token, src.twitter.config.access_token_secret)

api = tp.API(auth)

me = 3051592779

bfs_output_file = open("huge_network.txt", "a")


def dfs_fill_graph(file, start_user, current_level, end_level):

    if current_level < end_level:

        try:
            user_friends = api.followers_ids(start_user)
        except RateLimitError:

            print("Gone to sleep at {}! Be back soon.".format(datetime.datetime.now()))
            time.sleep((15 * 60) + 5)

            try:
                user_friends = api.followers_ids(start_user)
            except TweepError:
                return

        # The only reason we should encounter an error after sleeping is if the user is forbidden from being
        # accessed on the API for some reason.
        except TweepError:
            print("User is blocked from the Twitter API, going back up one level.")
            return

        edges = [(start_user, user_friend) for user_friend in user_friends]

        for (start_user, user_friend) in edges:
            print("Working on pair: {} {}".format(start_user, user_friend))
            file.write("{} {}\n".format(start_user, user_friend))

        for user in user_friends:
            dfs_fill_graph(file, user, current_level + 1, end_level)

    else:
        file.close()


def bfs_fill_graph(file, start_user):

    queue = list()
    visited = set()

    # Mark the source node as visited and enqueue it
    queue.append(start_user)

    while not len(queue) == 0:

        popped = queue.pop(0)

        visited.add(popped)

        # Get all the friends corresponding to the popped friend
        try:

            friends = api.followers_ids(popped)

        except RateLimitError:

            print("Gone to sleep at {}:{}! Be back soon.".format(datetime.datetime.now().hour,
                                                                datetime.datetime.now().minute))
            time.sleep((15 * 60) + 2)

            try:
                friends = api.followers_ids(popped)
            except TweepError:
                friends = []

        except TweepError:

            print("User is blocked from the Twitter API, continuing with the rest of the queue.")
            friends = []

        for friend in friends:

            if friend not in visited:
                queue.append(friend)

            visited.add(friend)
            print("Working on pair: {} {}".format(popped, friend))
            file.write("{} {}\n".format(popped, friend))

    file.close()


if __name__ == '__main__':

    try:
        bfs_fill_graph(bfs_output_file, me)
    except KeyboardInterrupt:
        print("Closing down...")
        bfs_output_file.close()
