import webbrowser


def shift_list(u_list, n):
    shifted_list = u_list.copy()
    if n >= 0:
        for i in range(n):
            shifted_list = shift_list_left(shifted_list)
    else:
        for i in range(abs(n)):
            shifted_list = shift_list_right(shifted_list)
    return shifted_list


def shift_list_right(u_list):
    s_list = u_list.copy()
    s_list[-1] = u_list[0]
    for i in range(0, len(u_list) - 1):
        s_list[i] = u_list[i + 1]
    u_list = s_list.copy()
    return u_list


def shift_list_left(u_list):
    s_list = u_list.copy()
    s_list[0] = u_list[-1]
    for i in range(1, len(u_list)):
        s_list[i] = u_list[i - 1]
    u_list = s_list.copy()
    return u_list


def unpack_data(message, index):
    crib = [chr(ord(each) + index) for each in message]
    return crib


def main():
    data = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
    data_list = data.split()

    new_list = [unpack_data(item, -1) for item in data_list]

    decoded_list = []
    i = 3
    for item in new_list:
        decoded_list.append(''.join(each for each in shift_list(item, i)))
        for each in item:
            if each == '.':
                i += 1

    original_data = ' '.join(item for item in decoded_list)

    url = "https://www.google.com/search?q={}".format(original_data)
    webbrowser.open_new_tab(url)


main()
