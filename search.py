from util import get_word

def get_posting_list(word, starting_pos, ending_pos, file_pointer):
    '''
        Get the posting list regarding the word using the secondary index
    which has the starting and ending positions(offsets of the file)
    of the starting alphabet of the word
        We do Binary Search on the positions

    @word : C{String}
    @primary_index_file_name : C{String}
    @secondary_index_file_name : C{String}

    @return : Returns the posting list of the word as a string
    '''

    l = int(starting_pos)
    r = int(ending_pos)
    while (l<r):
        m = (l+r)/2
        file_pointer.seek(m)
        # Read the partial string from (m to EOL)
        partial_string = file_pointer.readline()
        # Now file pointer is in a new line
        next_line = file_pointer.readline()
        # Get the token corresponding to next word
        this_word = get_word(next_line)
        if this_word == word:
            return next_line
        elif this_word < word:
            # The second half has to be traversed now
            l = m + 1
        else:
            # The left half has to be traversed now
            r = m - 1

    # Now l=r
    file_pointer.seek(l)
    line = file_pointer.readline()
    this_word = get_word(line)
    if this_word == word:
        return line
    else:
        return None
