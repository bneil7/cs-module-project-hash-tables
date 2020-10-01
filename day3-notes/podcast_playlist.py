# run_length (integers in minutes)
# podcast_episode_lengths = [] (list of integers)
# return Boolean whether there are two numbers in list whose sum == run_length
# user will not listen to same episode twice
#
def pod(total, podcasts):
    '''
    podcast_episode_lengths = {}

    for p in podcasts:
        podcast_episode_lengths[p] = True
    '''
    podcast_episode_lengths = set()

    for p in podcasts:
        podcast_episode_lengths.add(p)

    for p0 in podcasts:
        other_podcast_len = total - p0
        # is there a podcast of total - p0 minutes?
        if other_podcast_len in podcast_episode_lengths:
            return True

    return False


# total == 60
# p0 == 27
# p1 == 60 - 27 == total - p0 == 33
