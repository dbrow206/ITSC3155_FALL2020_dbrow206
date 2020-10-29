# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    counter = 0
    for i in emails:
        contacts[list(contacts.keys())[counter]] = i
        counter = counter + 1
        return contacts

    return


# # Part B.
def array2d_2_dict(contact_info, contacts):
    #
    if (len(contact_info) == 0):
        return contacts
    counter = 0

    for i in contact_info:
        if (len(i) == 0):
            return contacts
        contact = {"email": i[0], "phone": i[1]}
    contacts[list(contacts.keys())[counter]] = contact
    counter = counter + 1
    return contacts

    return


# # Part C.
def dict_2_array(contacts):
    nameArray=[]
    emailArray=[]
    phoneArray=[]

    if(len(list(contacts.keys())) ==0):
        return [[],[],[]]

    for i in list(contacts.keys()):
        nameArray.append(i)
        emailArray.append(contacts[i]['email'])
        phoneArray.append(contacts[i]['phone'])

    return[emailArray,phoneArray,nameArray]
    return
