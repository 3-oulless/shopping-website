#get user ip
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for :
        ip = x_forwarded_for.split(',')[0]
    else :
        ip = request.META.get('REMOTE_ADDR')
    return ip

def group_list(customer_list,size=4):
    grouped_list = []
    for i in range(0,len(customer_list),size):
        grouped_list.append(customer_list[i:i+size])
    return grouped_list