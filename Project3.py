import csv
import datetime
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
# from tkinter import messagebox
from tkcalendar import Calendar
root = Tk()
root.title("Facebook Inc.")
root.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

# Initial Frame.
myFrame = LabelFrame(root, padx=70, pady=70, text="Welcome to Facebook", font=("Roboto", 15), fg="#1877F2")
myFrame.pack(padx=50, pady=25)

# Login and Sign Up Buttons.
loginButton = Button(myFrame, text="Login", padx=30, pady=10, font=("Roboto", 12))
Label(myFrame, text="OR", font="Roboto", fg="#1877F2")
signButton = Button(myFrame, text="Sign Up", padx=30, pady=10, font=("Roboto", 12))

user_email = None
l1_info = {}
l2_info = {}
psfilepath = []
psImage = None
images = []
title_label = Label()
image_label = Label()
description_label = Label()
button_forward = Button()
button_back = Button()
private_filepath = r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\Post Private (1).png"
private_title = "None"
private_description = "None"
psfilepath1 = []
psImage1 = None
images1 = []
title_label1 = Label()
image_label1 = Label()
description_label1 = Label()
button_forward1 = Button()
button_back1 = Button()
psfilepath2 = []
psImage2 = None
images2 = []
title_label2 = Label()
image_label2 = Label()
description_label2 = Label()
button_forward2 = Button()
button_back2 = Button()
l3_info = {}
lpb = Button()
private_friends = []
pl1 = Label()
friend_to_add = Entry()
l4_info = {}
post_to_add = Entry()
private_lst = Entry()
button_comment = Button()
name_label = Label()
friend_request = []
request_to_accept = Entry()
request_to_reject = Entry()
l5_info = {}
acl = Label()
adl = Label()
ta = Button()
la = Button()
ta_info = {}
la_info = {}


class Post:

    post_id = 0

    def __init__(self):
        self.post_id = None
        self.post_type = None
        self.post_title = None
        self.post_description = None
        self.post_time = None
        self.post_date = None
        self.post_notification = 0
        self.post_recipients = 0
        self.privacy_id = 0
        self.page_id = None
        self.file_path = None

    @staticmethod
    def comment_on_a_post(post_id, u_ID, u_obj):
        commenting = Toplevel()
        commenting.title("Comment")
        commenting.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        pcFrame = LabelFrame(commenting, text="Add Comment", font=("Roboto", 15), fg="#1877F2", padx=40, pady=20)
        pcFrame.grid(row=0, column=0, sticky="W", padx=20, pady=20)

        def add_comment_now(chosen_post_id, ID, user_obj, comment_input):

            page_post_id = None
            is_page_post = False
            with open("Posts.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == chosen_post_id and row[12]:
                        is_page_post = True
                        page_post_id = row[12]
                        break

            if is_page_post:

                access = False
                with open("Page_Members.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[1] == str(user_obj.ID) and row[0] == page_post_id:
                            access = True

                with open("Pages.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(user_obj.ID) and row[3] == page_post_id:
                            access = True

                if access:
                    # Creating comment object.
                    comment = Comment()
                    # Setting attributes.
                    comment.receiver_id, comment.chosen_post_id = ID, chosen_post_id
                    comment.content, comment.sender_id = comment_input, user_obj.ID
                    comment.sender_first_name, comment.sender_last_name = user_obj.first_name, user_obj.last_name
                    # Storing comment data into a csv file.
                    with open("Comments.csv", "a", newline="") as data_file:
                        csv_writer = csv.writer(data_file, delimiter=",")
                        csv_writer.writerow(
                            [comment.receiver_id, comment.chosen_post_id, comment.content, comment.sender_id,
                             comment.sender_first_name, comment.sender_last_name, comment.pending])
                    Label(pcFrame, text="Comment Added.", font=("Roboto", 15), padx=7,
                          relief="groove").grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                    # Back.
                    Button(pcFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: commenting.destroy()).grid(row=3, column=0, pady=5, sticky="W")
                else:
                    Label(pcFrame, text="You can't comment on this post.", font=("Roboto", 15), padx=7,
                          relief="groove").grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                    # Back.
                    Button(pcFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: commenting.destroy()).grid(row=3, column=0, pady=5, sticky="W")
            else:
                # Creating comment object.
                comment = Comment()
                # Setting attributes.
                comment.receiver_id, comment.chosen_post_id = ID, chosen_post_id
                comment.content, comment.sender_id = comment_input, user_obj.ID
                comment.sender_first_name, comment.sender_last_name = user_obj.first_name, user_obj.last_name
                # Storing comment data into a csv file.
                with open("Comments.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow(
                        [comment.receiver_id, comment.chosen_post_id, comment.content, comment.sender_id,
                         comment.sender_first_name, comment.sender_last_name, comment.pending])
                Label(pcFrame, text="Comment Added.", font=("Roboto", 15), padx=7,
                      relief="groove").grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                # Back.
                Button(pcFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: commenting.destroy()).grid(row=3, column=0, pady=5, sticky="W")

        Label(pcFrame, text="Enter Comment: ", font=("Roboto", 15), padx=7). \
            grid(row=0, column=0, columnspan=2, padx=4, pady=5, sticky="W")

        comment_input = Entry(pcFrame, highlightthickness=2)
        comment_input.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        comment_input.grid(row=0, column=2, pady=5, sticky="E")

        Button(pcFrame, text="Add", font=("Roboto", 14), width=9, fg="#1877F2",
               command=lambda: add_comment_now(post_id, u_ID, u_obj, comment_input.get())).\
            grid(row=1, column=0, columnspan=3, pady=7, sticky="W")


class Comment:
    def __init__(self):
        self.receiver_id = None
        self.chosen_post_id = None
        self.content = None
        self.sender_id = None
        self.sender_first_name = None
        self.sender_last_name = None
        self.pending = True


class Friend:

    def __init__(self):

        self.first_name = None
        self.last_name = None
        self.pending = True


class Message:
    def __init__(self):
        self.receiver_ID = None
        self.sender_ID = None
        self.sender_first_name = None
        self.sender_last_name = None
        self.content = None
        self.pending = True


class Page:

    page_id = 0

    def __init__(self):
        self.page_id = None
        self.name = None
        self.category = None
        self.description = None
        self.creation_date = None
        self.users_who_liked = []


class User:

    users_id = 0
    privacy_lst_id = 0

    def __init__(self):

        self.first_name, self.last_name = None, None
        self.__email_or_phone = None
        self.__password = None
        self.ID = None
        self.gender, self.dob, self.about, self.current_city = None, None, None, None
        self.Education, self.Workplace, self.Relationship_Status = None, None, None
        self.online_status = False
        self.account_privacy = False

    def sign_up(self):
        top3 = Toplevel()
        top3.title("Sign up")
        top3.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        myFrame4 = LabelFrame(top3, text="Sign Up", font=("Roboto", 15), fg="#1877F2", padx=50, pady=40)
        myFrame4.pack(padx=20, pady=20)

        user_obj = self

        def clicked():

            email_phone = enter_email_phone.get()
            global user_email
            user_email = email_phone

            # Making sure the same email address or phone number isn't registered twice.
            repetition = False
            with open("Users_Database.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == email_phone:
                        repetition = True
                        break

            if repetition:

                def login_instead(obj):
                    top3.destroy()
                    obj.login()

                Label(myFrame4, text="Account already registered.", font=("Roboto", 13), relief="groove").\
                    grid(row=2, column=0, columnspan=2, sticky="W")
                Label(myFrame4, text="Login instead!", font=("Roboto", 13), relief="groove"). \
                    grid(row=3, column=0, columnspan=2, sticky="W")
                Button(myFrame4, text="Login", font=("Roboto", 13), width=12, bg="#1877F2", fg="white",
                       command=lambda: login_instead(user_obj)).grid(row=4, column=0, columnspan=2, pady=12, sticky="W")

            else:
                top3.destroy()
                top4 = Toplevel()
                top4.title("Sign Up")
                top4.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

                myFrame5 = LabelFrame(top4, text="Sign Up", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
                myFrame5.pack(padx=20, pady=20)

                Label(myFrame5, text="Password", font=("Roboto", 15), padx=7). \
                    grid(row=0, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                Label(myFrame5, text="First Name", font=("Roboto", 15), padx=7). \
                    grid(row=1, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                Label(myFrame5, text="Last Name", font=("Roboto", 15), padx=7). \
                    grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                Label(myFrame5, text="Gender", font=("Roboto", 15), padx=7).\
                    grid(row=3, column=0, columnspan=2, padx=4, pady=(5, 0), sticky="W")
                Label(myFrame5, text="Date of Birth", font=("Roboto", 15), padx=7). \
                    grid(row=5, column=0, columnspan=2, padx=4, pady=5, sticky="W")

                user_password = Entry(myFrame5, highlightthickness=2)
                user_password.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_first_name = Entry(myFrame5, highlightthickness=2)
                user_first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_last_name = Entry(myFrame5, highlightthickness=2)
                user_last_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

                user_gender = StringVar()
                user_gender.set("Male")
                Radiobutton(myFrame5, text="Male", variable=user_gender, font=("Helvetica 18 bold", 12),
                            value="Male", fg="#1877F2").grid(row=4, column=0, pady=5, sticky="W")
                Radiobutton(myFrame5, text="Female", variable=user_gender, font=("Helvetica 18 bold", 12),
                            value="Female", fg="#1877F2").grid(row=4, column=1, pady=5, sticky="W")
                Radiobutton(myFrame5, text="Other", variable=user_gender, font=("Helvetica 18 bold", 12), value="Other",
                            fg="#1877F2").grid(row=4, column=2, pady=5, sticky="W")

                cal = Calendar(myFrame5, selectmode='day', year=2020, month=5, day=22)
                cal.grid(row=6, column=2, pady=5, sticky="E", padx=15)

                user_password.grid(row=0, column=2, pady=5, sticky="E")
                user_first_name.grid(row=1, column=2, pady=5, sticky="E")
                user_last_name.grid(row=2, column=2, pady=5, sticky="E")

                l1 = Label(myFrame5, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                           padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

                def sign_up_now():

                    global l1_info

                    if user_password.index("end") == 0 or user_first_name.index("end") == 0 or user_last_name.index\
                                ("end") == 0:
                        l1.grid(row=8, column=0, columnspan=2, pady=5, padx=3, sticky="W")
                        l1_info = l1.grid_info()
                    else:
                        if l1_info != {}:
                            if l1_info["row"] == 8:
                                l1.destroy()
                        # Setting object's attributes after data has been entered.
                        self.__email_or_phone = user_email
                        self.__password = user_password.get()
                        self.first_name = user_first_name.get()
                        self.last_name = user_last_name.get()
                        self.dob = cal.get_date()
                        self.gender = user_gender.get()

                        # Each user gets a unique user id.
                        r = csv.reader(open("Users_Database.csv"))
                        lines = list(r)
                        for lst in range(1, len(lines)):
                            if lines[lst][0]:
                                User.users_id = lines[lst][0]
                        self.ID = int(User.users_id) + 1

                        with open("Users_Database.csv", "a", newline="") as data_file:
                            csv_writer = csv.writer(data_file, delimiter=",")
                            csv_writer.writerow(
                                [self.ID, self.first_name, self.last_name, self.__email_or_phone, self.__password,
                                 self.gender, self.dob, self.about, self.current_city, self.Education,
                                 self.Workplace, self.Relationship_Status, self.account_privacy])

                        # Signed in notification.
                        Label(myFrame5, text="You're signed in!", font=("Roboto", 15)). \
                            grid(row=8, column=0, columnspan=2, pady=5, padx=3, sticky="W")

                        def login_after_signup(obj):
                            top4.destroy()
                            obj.login()

                        def exit():
                            top4.destroy()

                        # Actions to take after profile has been created.
                        Button(myFrame5, text="Login", font=("Roboto", 14), width=10, bg="#1877F2", fg="white",
                               command=lambda: login_after_signup(user_obj)).grid(row=9, column=0, columnspan=2, pady=5,
                                                                                  sticky="W")
                        Button(myFrame5, text="Exit", font=("Roboto", 14), width=10, fg="#1877F2", command=exit).\
                            grid(row=9, column=2, pady=5, sticky="W")

                Button(myFrame5, text="Enter", font=("Roboto", 14), width=9, fg="#1877F2", command=sign_up_now).\
                    grid(row=7, column=0, columnspan=3, pady=7, sticky="W")

        myLabel = Label(myFrame4, text="Email Address", font=("Roboto", 13), padx=20, pady=4, bd=1, relief="sunken")
        myButton = Button(myFrame4, text="Enter", font=("Roboto", 13), width=7, padx=2, fg="#1877F2", command=clicked)
        enter_email_phone = Entry(myFrame4, highlightthickness=2)
        enter_email_phone.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

        myLabel.grid(row=0, column=0, padx=7, sticky="W")
        myButton.grid(row=1, column=0, pady=12, sticky="W")
        enter_email_phone.grid(row=0, column=1, sticky="E")

    def login(self):

        user_obj = self

        top = Toplevel()
        top.title("Login")
        top.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        myFrame2 = LabelFrame(top, text="Login", font=("Roboto", 15), fg="#1877F2", padx=50, pady=40)
        myFrame2.pack(padx=30, pady=30)

        def info_entered():
            email_phone = enter_email_phone.get()
            password = enter_password.get()

            registered = False
            with open("Users_Database.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == email_phone:
                        self.ID, self.first_name, self.last_name = row[0], row[1], row[2]
                        self.__email_or_phone, self.__password = row[3], row[4]
                        self.gender, self.dob, self.about, self.current_city = row[5], row[6], row[7], row[8]
                        self.Education, self.Workplace, self.Relationship_Status = row[9], row[10], row[11]
                        self.account_privacy = row[12]
                        registered = True
                        break

            if registered:
                match = False
                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[3] == email_phone and row[4] == password:
                            match = True
                            break

                if match:
                    # Destroy the old window.
                    # Create a new window.
                    # Put all the features there.
                    Label(myFrame2, text="You are Logged in!", font=("Roboto", 12)).grid(row=3, column=0, columnspan=2,
                                                                                         sticky="W")
                    # Creating user's home page.
                    top.destroy()
                    home = Toplevel()
                    home.title("Home Page")
                    home.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

                    def see_messages(obj):
                        obj.see_user_messages()

                    def see_friends(obj):
                        obj.view_user_friends()

                    # Displaying user's profile information.
                    profile_info = LabelFrame(home, text="Profile Info", font=("Roboto", 15), fg="#1877F2", padx=20,
                                              pady=10)
                    profile_info.grid(row=0, column=0, padx=20, pady=20, sticky="W")

                    Label(profile_info, text=self.first_name + " " + self.last_name, font=("Roboto", 14)).\
                        grid(row=0, column=0, pady=5, sticky="W")

                    Label(profile_info, text="About:", font=("Roboto", 12)).grid(row=1, column=0, pady=3, sticky="W")
                    Label(profile_info, text=self.about, font=("Helvetica", 12)).grid(row=1, column=1, pady=3,
                                                                                      sticky="W")
                    Label(profile_info, text="Current City: ", font=("Roboto", 12)).grid(row=2, column=0,  pady=3,
                                                                                         sticky="W")
                    Label(profile_info, text=self.current_city, font=("Helvetica", 12)).grid(row=2, column=1, pady=3,
                                                                                             sticky="W")
                    Label(profile_info, text="Education: ", font=("Roboto", 12)).grid(row=3, column=0, pady=3,
                                                                                      sticky="W")
                    Label(profile_info, text=self.Education, font=("Helvetica", 12)).grid(row=3, column=1,  pady=3,
                                                                                          sticky="W")
                    Label(profile_info, text="Workplace: ", font=("Roboto", 12)).grid(row=4, column=0, pady=3,
                                                                                      sticky="W")
                    Label(profile_info, text=self.Workplace, font=("Helvetica", 12)).grid(row=4, column=1,  pady=3,
                                                                                          sticky="W")
                    Label(profile_info, text="Relationship Status: ", font=("Roboto", 12)).grid(row=5, column=0, pady=3,
                                                                                                sticky="W")
                    Label(profile_info, text=self.Relationship_Status, font=("Helvetica", 12)).grid(row=5, column=1,
                                                                                                    pady=3, sticky="W")

                    # Displaying user's posts.
                    profile_posts = LabelFrame(home, text="Posts", font=("Roboto", 15), fg="#1877F2", padx=30, pady=10)
                    profile_posts.grid(row=1, column=0, padx=20, pady=20, sticky="W")

                    pstitle = []
                    psdescription = []
                    global psfilepath
                    global psImage
                    global images
                    global title_label
                    global image_label
                    global description_label
                    global button_forward
                    global button_back
                    images.clear()
                    psfilepath.clear()

                    post_num = 1

                    has_posts = False
                    with open("Posts.csv") as data_file:
                        csv_reader = csv.reader(data_file, delimiter=",")
                        for row in csv_reader:
                            if row[0] == self.ID and not row[12]:
                                pstitle.append(row[5])
                                psdescription.append(row[6])
                                psfilepath.append(row[13])
                                has_posts = True

                    if has_posts:
                        for pic in psfilepath:
                            my_pic = Image.open(pic)
                            resized = my_pic.resize((320, 220))
                            new_pic = ImageTk.PhotoImage(resized)
                            images.append(new_pic)

                        title_label = Label(profile_posts, text=pstitle[post_num-1], font=("Roboto", 13), padx=7,
                                            pady=5)
                        image_label = Label(profile_posts, image=images[post_num-1])
                        description_label = Label(profile_posts, text=psdescription[post_num-1],
                                                  font=("Helvetica bold 18", 13), padx=7, pady=3)

                        def forward(p_num):
                            global title_label
                            global image_label
                            global description_label
                            global button_forward
                            global button_back
                            global images

                            title_label.grid_forget()
                            image_label.grid_forget()
                            description_label.grid_forget()

                            title_label = Label(profile_posts, text=pstitle[p_num - 1], font=("Roboto", 13), padx=7,
                                                pady=5)
                            image_label = Label(profile_posts, image=images[p_num - 1])
                            description_label = Label(profile_posts, text=psdescription[p_num - 1],
                                                      font=("Helvetica bold 18", 13), padx=7, pady=3)

                            button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                    fg="#1877F2", command=lambda: forward(p_num+1))
                            button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: back(p_num-1))

                            if p_num == len(images):
                                button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                        state="disabled")

                            title_label.grid(row=0, column=0, sticky="W")
                            image_label.grid(row=1, column=0, columnspan=2, sticky="W")
                            description_label.grid(row=2, column=0, sticky="W", pady=7)
                            button_forward.place(x=250, y=295)
                            button_back.grid(row=3, column=0, sticky="W")

                        def back(p_num):
                            global title_label
                            global image_label
                            global description_label
                            global button_forward
                            global button_back
                            global images

                            title_label.grid_forget()
                            image_label.grid_forget()
                            description_label.grid_forget()

                            title_label = Label(profile_posts, text=pstitle[p_num - 1], font=("Roboto", 13), padx=7,
                                                pady=5)
                            image_label = Label(profile_posts, image=images[p_num - 1])
                            description_label = Label(profile_posts, text=psdescription[p_num - 1],
                                                      font=("Helvetica bold 18", 13), padx=7, pady=3)

                            button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                    fg="#1877F2", command=lambda: forward(p_num + 1))
                            button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: back(p_num - 1))

                            if p_num == 1:
                                button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13),
                                                     state="disabled")

                            title_label.grid(row=0, column=0, sticky="W")
                            image_label.grid(row=1, column=0, columnspan=2, sticky="W")
                            description_label.grid(row=2, column=0, sticky="W", pady=7)
                            button_forward.place(x=250, y=295)
                            button_back.grid(row=3, column=0, sticky="W")

                        if len(images) != 1:
                            button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                    fg="#1877F2", command=lambda: forward(post_num + 1))
                            button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: back(post_num))
                        else:
                            button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                    fg="#1877F2", state="disabled")
                            button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 state="disabled")

                        title_label.grid(row=0, column=0, sticky="W")
                        image_label.grid(row=1, column=0, columnspan=2, sticky="W")
                        description_label.grid(row=2, column=0, sticky="W", pady=7)
                        button_forward.place(x=250, y=295)
                        button_back.grid(row=3, column=0, sticky="W")

                    if not has_posts:

                        Label(profile_posts, text="You've no posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3,
                                                                                                sticky="W")

                    # Displaying user's messages.
                    see = LabelFrame(home, text="See", font=("Roboto", 15), fg="#1877F2", padx=30, pady=10)
                    see.grid(row=0, column=1, padx=15, pady=5, sticky="E")

                    Button(see, text="Messages", width=14, font=("Roboto", 13), command=lambda:
                    see_messages(user_obj)).grid(row=0, column=0, pady=4, sticky="W")
                    Button(see, text="Friends", width=14, font=("Roboto", 13), command=lambda: see_friends(user_obj)). \
                        grid(row=1, column=0, pady=4, sticky="W")

                    def edit_profile(obj):
                        obj.edit_user()

                    def change_privacy(obj):
                        obj.change_account_privacy()

                    def block(obj):
                        obj.block_a_user()

                    def unblock(obj):
                        obj.unblock_a_user()

                    def make_private_list(obj):
                        obj.create_privacy_list()

                    def post_private(obj):
                        obj.make_a_post_private()

                    def account_privacy():
                        privacy = Toplevel()
                        privacy.title("Privacy Settings")
                        privacy.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

                        prFrame = LabelFrame(privacy, text="Privacy Settings", font=("Roboto", 15), fg="#1877F2",
                                             padx=50, pady=30)
                        prFrame.pack(padx=20, pady=20)

                        # Change account privacy.
                        Button(prFrame, text="Privacy", width=14, font=("Roboto", 13),
                               command=lambda: change_privacy(user_obj)).grid(row=0, column=0, pady=5, sticky="W")
                        # Block a user.
                        Button(prFrame, text="Block User", width=14, font=("Roboto", 13),
                               command=lambda: block(user_obj)).grid(row=1, column=0, pady=5, sticky="W")
                        # Unblock a user.
                        Button(prFrame, text="Unblock User", width=14, font=("Roboto", 13),
                               command=lambda: unblock(user_obj)).grid(row=2, column=0, pady=5, sticky="W")
                        # Create a privacy list.
                        Button(prFrame, text="Privacy List", width=14, font=("Roboto", 13),
                               command=lambda: make_private_list(user_obj)).grid(row=3, column=0, pady=5, sticky="W")
                        # Make a post private.
                        Button(prFrame, text="Post Privacy", width=14, font=("Roboto", 13),
                               command=lambda: post_private(user_obj)).grid(row=4, column=0, pady=5, sticky="W")
                        # Back.
                        Button(prFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                               command=lambda: privacy.destroy()).grid(row=5, column=0, pady=5, sticky="W")

                    def delete_profile(obj):
                        obj.delete_user()
                        home.destroy()

                    def settings():
                        # Settings window.
                        setting = Toplevel()
                        setting.title("Settings")
                        setting.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

                        setFrame = LabelFrame(setting, text="Settings", font=("Roboto", 15), fg="#1877F2", padx=50,
                                              pady=30)
                        setFrame.pack(padx=40, pady=40)

                        # Edit profile.
                        Button(setFrame, border=1, text="Edit Profile", width=14, font=("Roboto", 13),
                               command=lambda: edit_profile(user_obj)).grid(row=0, column=0, pady=5, sticky="W")
                        # Change account privacy.
                        Button(setFrame, text="Account Privacy", width=14, font=("Roboto", 13),
                               command=account_privacy).grid(row=1, column=0, pady=5, sticky="W")
                        # Delete profile.
                        Button(setFrame, text="Delete Profile", width=14, font=("Roboto", 13), fg="#1877F2",
                               command=lambda: delete_profile(user_obj)).grid(row=2, column=0, pady=5, sticky="W")
                        # Back.
                        Button(setFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                               command=lambda: setting.destroy()).grid(row=3, column=0, pady=5, sticky="W")

                    def search_a_user(obj):
                        obj.search_user()

                    def search_a_page(obj):
                        obj.search_page()

                    def send_request(obj):
                        obj.add_friend()

                    def send_message(obj):
                        obj.send_message()

                    def log_out(obj):
                        obj.logout()
                        home.destroy()

                    def create_post(obj):
                        obj.create_a_post()

                    def create_page(obj):
                        obj.create_a_page()

                    def search():
                        # Search window.
                        searchWindow = Toplevel()
                        searchWindow.title("Search")
                        searchWindow.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

                        searchFrame = LabelFrame(searchWindow, text="Search", font=("Roboto", 15), fg="#1877F2",
                                                 padx=50, pady=30)
                        searchFrame.pack(padx=20, pady=20)

                        # Search a user's profile.
                        Button(searchFrame, text="Search User", width=14, font=("Roboto", 13),
                               command=lambda: search_a_user(user_obj)).grid(row=0, column=0, pady=5, sticky="W")
                        # Search a page.
                        Button(searchFrame, text="Search Page", width=14, font=("Roboto", 13),
                               command=lambda: search_a_page(user_obj)).grid(row=1, column=0, pady=5, sticky="W")
                        # Back.
                        Button(searchFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                               command=lambda: searchWindow.destroy()).grid(row=2, column=0, pady=5, sticky="W")

                    # Displaying all the options.
                    options = LabelFrame(home, text="Do", font=("Roboto", 15), fg="#1877F2", padx=30, pady=10)
                    options.grid(row=1, column=1, padx=15, pady=15, sticky="E")

                    Button(options, text="Settings", width=14, font=("Roboto", 13), command=settings). \
                        grid(row=0, column=0, pady=4, sticky="W")
                    Button(options, text="Search", width=14, font=("Roboto", 13), command=search). \
                        grid(row=1, column=0, pady=2, sticky="W")
                    Button(options, text="Send Request", width=14, font=("Roboto", 13),
                           command=lambda:send_request(user_obj)).grid(row=2, column=0, pady=4, sticky="W")
                    Button(options, text="Send Message", width=14, font=("Roboto", 13),
                           command=lambda: send_message(user_obj)).grid(row=3, column=0, pady=4, sticky="W")
                    Button(options, text="Logout", width=14, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: log_out(user_obj)).grid(row=4, column=0, pady=4, sticky="W")

                    # Displaying creating options.
                    create = LabelFrame(home, text="Create", font=("Roboto", 15), fg="#1877F2", padx=30, pady=10)
                    create.grid(row=0, column=2, padx=20, pady=20, sticky="W")

                    Button(create, text="Post", width=14, font=("Roboto", 13), command= lambda: create_post(user_obj)).\
                        grid(row=0, column=0, pady=4, sticky="W")
                    Button(create, text="Page", width=14, font=("Roboto", 13), command= lambda: create_page(user_obj)).\
                        grid(row=1, column=0, pady=4, sticky="W")

                    self.online_status = True

                    self.accept_decline_friend_request()
                    self.notifications()

                else:

                    def password_reset(obj):
                        top.destroy()
                        obj.user_update()

                    def login_again(obj):
                        top.destroy()
                        obj.login()

                    Label(myFrame2, text="Incorrect Information!", font=("Roboto", 13)).\
                        grid(row=4, column=0, columnspan=2, pady=5)
                    resetButton = Button(myFrame2, text="Reset Password", width=15, font=("Roboto", 13), fg="#1877F2",
                                         command=lambda: password_reset(user_obj))
                    tryButton = Button(myFrame2, text="Try again", width=13, font=("Roboto", 13), fg="#1877F2",
                                       command=lambda: login_again(user_obj))

                    resetButton.grid(row=5, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                    Label(myFrame2, text="OR", font=("Roboto", 13)).grid(row=6, column=0, columnspan=2, pady=5)
                    tryButton.grid(row=7, column=0, columnspan=2, padx=3, sticky="W")

            else:
                Label(myFrame2, text="Sign Up First!", font=("Roboto", 13)).grid(row=4, column=0, columnspan=2, pady=5)
                signUpButton = Button(myFrame2, text="Sign Up", width=14, font=("Roboto", 13), fg="#1877F2")
                ExitButton = Button(myFrame2, text="Exit", width=14, font=("Roboto", 13), fg="#1877F2")

                signUpButton.grid(row=5, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                Label(myFrame2, text="OR", font=("Roboto", 12)).grid(row=6, column=0, columnspan=2)
                ExitButton.grid(row=7, column=0, columnspan=2, padx=3, sticky="W")

        myLabel1 = Label(myFrame2, text="Email or Phone", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken")
        myLabel2 = Label(myFrame2, text="Password", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken")
        myButton = Button(myFrame2, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2", command=info_entered)

        enter_email_phone = Entry(myFrame2, highlightthickness=2)
        enter_email_phone.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        enter_password = Entry(myFrame2, highlightthickness=2)
        enter_password.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

        myLabel1.grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")
        myLabel2.grid(row=1, column=0, columnspan=2, padx=3, sticky="W")
        myButton.grid(row=2, column=0, pady=12, sticky="W")
        enter_email_phone.grid(row=0, column=2, sticky="E")
        enter_password.grid(row=1, column=2, sticky="E")

    def logout(self):
        self.online_status = False

    # Edit your profile.
    def edit_user(self):
        edit = Toplevel()
        edit.title("Edit Profile")

        editFrame = LabelFrame(edit, text="Edit Profile", font=("Roboto", 15), fg="#1877F2", padx=50, pady=40)
        editFrame.pack(padx=20, pady=20)

        Label(editFrame, text="About", font=("Roboto", 13), padx=7).grid(row=0, column=0, columnspan=2, pady=5,
                                                                         sticky="W")
        Label(editFrame, text="City", font=("Roboto", 13), padx=7).grid(row=1, column=0, columnspan=2, pady=5,
                                                                        sticky="W")
        Label(editFrame, text="Workplace", font=("Roboto", 13), padx=7).grid(row=2, column=0, columnspan=2, pady=5,
                                                                             sticky="W")
        Label(editFrame, text="Education", font=("Roboto", 13), padx=7).grid(row=3, column=0, columnspan=2, pady=5,
                                                                             sticky="W")
        Label(editFrame, text="Relationship Status", font=("Roboto", 13), padx=7).grid(row=4, column=0, columnspan=2,
                                                                                       pady=5, sticky="W")
        # Getting previous values.
        with open("Users_Database.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID):
                    about = row[7]
                    city = row[8]
                    ed = row[9]
                    wp = row[10]
                    rs = row[11]

        user_about = Entry(editFrame, highlightthickness=2)
        user_about.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_about.insert(0, about)
        user_city = Entry(editFrame, highlightthickness=2)
        user_city.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_city.insert(0, city)
        user_workplace = Entry(editFrame, highlightthickness=2)
        user_workplace.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_workplace.insert(0, wp)
        user_education = Entry(editFrame, highlightthickness=2)
        user_education.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_education.insert(0, ed)
        user_relationship = Entry(editFrame, highlightthickness=2)
        user_relationship.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_relationship.insert(0, rs)

        user_about.grid(row=0, column=2, sticky="E")
        user_city.grid(row=1, column=2, sticky="E")
        user_workplace.grid(row=2, column=2, sticky="E")
        user_education.grid(row=3, column=2, sticky="E")
        user_relationship.grid(row=4, column=2, sticky="E")

        def edit_now():
            self.about = user_about.get()
            self.current_city = user_city.get()
            self.Workplace = user_workplace.get()
            self.Education = user_education.get()
            self.Relationship_Status = user_relationship.get()

            # Updating user's info in the database.
            r = csv.reader(open("Users_Database.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][0] == str(self.ID):
                    lines[lst][7], lines[lst][8], lines[lst][9] = self.about, self.current_city, self.Education
                    lines[lst][10], lines[lst][11] = self.Workplace, self.Relationship_Status
                    break
            writer = csv.writer(open("Users_Database.csv", "w", newline=""))
            writer.writerows(lines)
            Label(editFrame, text="Profile Updated!", font=("Roboto", 14), pady=8).\
                grid(row=6, column=0, columnspan=2, pady=5, sticky="W")
            # Back.
            Button(editFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: edit.destroy()).grid(row=7, column=0, pady=3, sticky="W")

        Button(editFrame, text="Done", font=("Roboto", 13), width=7, fg="#1877F2", command=edit_now).\
            grid(row=5, column=0, columnspan=3, sticky="W", pady=10)

    # View your posts.
    def view_user_posts(self):
        posts = []
        with open("Posts.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == self.ID and not row[12]:
                    posts.append(row[3])
        return posts

    def see_user_messages(self):
        seeing_messages = Toplevel()
        seeing_messages.title("See Message")
        seeing_messages.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        reFrame = LabelFrame(seeing_messages, text="Received", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        reFrame.grid(row=0, column=0, sticky="W", padx=20, pady=15)

        seFrame = LabelFrame(seeing_messages, text="Sent", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        seFrame.grid(row=1, column=0, sticky="W", padx=20, pady=15)

        received = False
        with open("Message.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID):
                    received = True
                    break

        if received:
            row_no = 0
            with open("Message.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID):
                        Label(reFrame, text=f"{row[4]}", font=("Roboto", 13), padx=20, pady=5,
                              bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=2, padx=3,
                                                          sticky="W")
                        Label(reFrame, text=f"From {row[2]} {row[3]}", font=("Roboto", 13), padx=20, pady=5,
                              fg="#1877F2", bd=1, relief="groove").grid(row=row_no+1, column=0, columnspan=2,
                                                                        pady=(2, 5), padx=3, sticky="W")
                        row_no += 1
        else:
            Label(reFrame, text="No messages received.", font=("Roboto", 14), padx=20, pady=5,
                  bd=1, relief="groove").grid(row=0, column=0, columnspan=2, pady=2, padx=3,
                                              sticky="W")

        sent = False
        with open("Message.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[1] == str(self.ID):
                    sent = True
                    break

        if sent:
            row_no = 0
            with open("Message.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[1] == str(self.ID):
                        Label(seFrame, text=f"{row[4]}", font=("Roboto", 13), padx=20, pady=5,
                              bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=2, padx=3,
                                                          sticky="W")
                        row_no += 1
        else:
            Label(seFrame, text="No messages sent.", font=("Roboto", 14), padx=20, pady=5,
                  bd=1, relief="groove").grid(row=0, column=0, columnspan=2, pady=2, padx=3,
                                              sticky="W")

    # View your friends.
    def view_user_friends(self):
        seeing_friends = Toplevel()
        seeing_friends.title("See Friends")
        seeing_friends.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        sfFrame = LabelFrame(seeing_friends, text="Friends", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        sfFrame.grid(row=0, column=0, sticky="W", padx=20, pady=15)

        has_friends = False
        with open("Friends.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID) and row[6] == str(False):
                    has_friends = True
                elif row[3] == str(self.ID) and row[6] == str(False):
                    has_friends = True

        if has_friends:

            row_no = 0
            with open("Friends.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID) and row[6] == str(False):
                        Label(sfFrame, text=f"{row[4]} {row[5]}", font=("Roboto", 13), padx=20, pady=5,
                              bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=2, padx=3,
                                                          sticky="W")
                        row_no += 1
                    elif row[3] == str(self.ID) and row[6] == str(False):
                        Label(sfFrame, text=f"{row[1]} {row[2]}", font=("Roboto", 13), padx=20, pady=5,
                              bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=2, padx=3,
                                                          sticky="W")
                        row_no += 1
        else:
            Label(sfFrame, text="You've no friends.", font=("Roboto", 13), padx=20, pady=5,
                  bd=1, relief="groove").grid(row=0, column=0, columnspan=2, pady=2, padx=3,
                                              sticky="W")

    def set_account_privacy(self, value):
        self.account_privacy = value

    # Make your account private or public.
    def change_account_privacy(self):
        user_obj = self

        account_privacy = Toplevel()
        account_privacy.title("Account Privacy")
        account_privacy.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        apFrame = LabelFrame(account_privacy, text="Change Account Privacy", font=("Roboto", 15), fg="#1877F2",
                             padx=50, pady=40)
        apFrame.pack(padx=20, pady=20)

        def make_public(obj):
            obj.set_account_privacy(False)
            Label(apFrame, text="Status Updated!", font=("Roboto", 13), padx=7). \
                grid(row=2, column=0, columnspan=2, pady=5, sticky="W")
            Button(apFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: account_privacy.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        def make_private(obj):
            obj.set_account_privacy(True)
            Label(apFrame, text="Status Updated!", font=("Roboto", 13), padx=7). \
                grid(row=2, column=0, columnspan=2, pady=5, sticky="W")
            Button(apFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: account_privacy.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        if self.account_privacy == str(True):
            Label(apFrame, text="Your account is private.", font=("Roboto", 13), padx=7).\
                grid(row=0, column=0, columnspan=2, pady=5, sticky="W")
            Button(apFrame, text="Make Public", font=("Roboto", 13), width=14, fg="#1877F2",
                   command=lambda: make_public(user_obj)).grid(row=1, column=0, columnspan=2, padx=4,
                                                               pady=7, sticky="W")

        else:
            Label(apFrame, text="Your account is public.", font=("Roboto", 13), padx=7). \
                grid(row=0, column=0, columnspan=2, pady=5, sticky="W")
            Button(apFrame, text="Make Private", font=("Roboto", 13), width=14, fg="#1877F2",
                   command=lambda: make_private(user_obj)).grid(row=1, column=0, columnspan=2, padx=4,
                                                                pady=7, sticky="W")

        # Updating account privacy in the database.
        r = csv.reader(open("Users_Database.csv"))
        lines = list(r)
        for lst in range(len(lines)):
            if lines[lst][0] == str(self.ID):
                lines[lst][12] = self.account_privacy
                break
        writer = csv.writer(open("Users_Database.csv", "w", newline=""))
        writer.writerows(lines)

    # Update your password in the database.
    def user_update(self):
        user_obj = self

        update = Toplevel()
        update.title("Update Info.")
        update.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        upFrame = LabelFrame(update, text="Reset Password", font=("Roboto", 15), fg="#1877F2",
                             padx=50, pady=40)
        upFrame.pack(padx=20, pady=20)

        Label(upFrame, text="Email or Phone", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken").\
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        email_phone = Entry(upFrame, highlightthickness=2)
        email_phone.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        email_phone.grid(row=0, column=2, sticky="E")

        def login_again(obj):
            update.destroy()
            obj.login()

        def try_again(obj):
            update.destroy()
            obj.user_update()

        def password_entered(new):
            self.__password = new

            # Updating user's password in the database.
            r = csv.reader(open("Users_Database.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][0] == str(self.ID):
                    lines[lst][4] = self.__password
                    break
            writer = csv.writer(open("Users_Database.csv", "w", newline=""))
            writer.writerows(lines)

            Label(upFrame, text="Password Updated!", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
                grid(row=3, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            Button(upFrame, text="Login", font=("Roboto", 13), width=12, fg="#1877F2",
                   command=lambda: login_again(user_obj)).grid(row=4, column=0, columnspan=3, pady=10, sticky="W")

        def info_entered():
            found = False
            with open("Users_Database.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == email_phone.get():
                        self.ID = row[0]
                        found = True

            if found:
                b1.destroy()

                Label(upFrame, text="Password", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
                    grid(row=1, column=0, columnspan=2, pady=10, padx=3, sticky="W")

                new_password = Entry(upFrame, highlightthickness=2)
                new_password.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                new_password.grid(row=1, column=2, sticky="E")

                Button(upFrame, text="Update", font=("Roboto", 13), width=7, fg="#1877F2",
                       command=lambda: password_entered(new_password.get())).grid(row=2, column=0, columnspan=3, pady=5,
                                                                                  sticky="W")
            else:
                Label(upFrame, text="Incorrect Information. Try again!", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken").grid(row=2, column=0, columnspan=2, pady=10, padx=3, sticky="W")

                Button(upFrame, text="Try Again", font=("Roboto", 13), width=12, fg="#1877F2",
                       command=lambda: try_again(user_obj)).grid(row=3, column=0, columnspan=3, pady=5, sticky="W")

        b1 = Button(upFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2", command=info_entered)
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    # Find other users in the database by their first name.
    def find_users(self, first_name):
        users = []
        # Finding all users with the first name that you searched for.
        with open("Users_Database.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[1] == first_name and row[0] != str(self.ID):
                    users.append(row[0])

        # Excluding those who've blocked you.
        with open("Blocked_Users.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[1] == str(self.ID) and row[0] in users:
                    users.remove(row[0])
        return users

    # Search for another user by their first name.
    def search_user(self):
        search_user_win = Toplevel()
        search_user_win.title("Search User")
        search_user_win.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        sFrame = LabelFrame(search_user_win, text="Search a user", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        sFrame.pack(padx=20, pady=20)

        Label(sFrame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(sFrame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def search_now(user_ID, users, row_no):
            ID = users[user_ID - 1]
            # Checking if the user you are searching for hasn't blocked you.
            access = True
            with open("Blocked_Users.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == ID and row[1] == self.ID:
                        access = False
                        break
            if access:
                search_user_win.destroy()
                return self.display_user_profile(ID)
            else:
                Label(sFrame, text="Search Blocked.", font=("Roboto", 13), padx=20, pady=5). \
                    grid(row=row_no + 3, column=0, columnspan=3, pady=7, sticky="W")

        def info_entered(name):
            users = self.find_users(name)

            if users:
                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(sFrame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20, pady=5,
                                  bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10, padx=3,
                                                              sticky="W")
                            row_no += 1

                Label(sFrame, text="Number of profile\nyou want to see: ", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken", fg="#1877F2").grid(row=row_no+1, column=0, columnspan=2, pady=10, padx=3,
                                                          sticky="W")

                user_to_see = Entry(sFrame, highlightthickness=2)
                user_to_see.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_see.grid(row=row_no+1, column=2, sticky="E")

                b2 = Button(sFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: search_now(int(user_to_see.get()), users, row_no))
                b2.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")

            else:
                Label(sFrame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken", fg="#1877F2").grid(row=2, column=0, columnspan=2, pady=10, padx=3,
                                                          sticky="W")

        b1 = Button(sFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    # Delete your profile.
    def delete_user(self):
        # Deleting user's account from the database.
        r = csv.reader(open("Users_Database.csv"))
        lines = list(r)
        for lst in range(len(lines)):
            if lines[lst][0] == str(self.ID):
                lines.remove(lines[lst])
                break
        writer = csv.writer(open("Users_Database.csv", "w", newline=""))
        writer.writerows(lines)
        print("Account deleted.")

    # Block another user.
    def block_a_user(self):
        block = Toplevel()
        block.title("Block")
        block.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        bFrame = LabelFrame(block, text="Block a User", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        bFrame.pack(padx=20, pady=20)

        Label(bFrame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(bFrame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def block_now(user_ID, users, row_no):
            ID = users[user_ID - 1]
            # Checking if the user isn't already blocked.
            blocked = False
            with open("Blocked_Users.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == self.ID and row[1] == ID:
                        blocked = True
                        break
            # Blocking the user.
            if not blocked:
                with open("Blocked_Users.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow([self.ID, ID])
                Label(bFrame, text="User blocked.", font=("Roboto", 13), padx=20, pady=5).\
                    grid(row=row_no+3, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(bFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: block.destroy()).grid(row=row_no+4, column=0, pady=3, sticky="W")
            else:
                Label(bFrame, text="User is already blocked.", font=("Roboto", 13), padx=20, pady=5).\
                    grid(row=row_no+3, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(bFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: block.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")

        def info_entered(name):
            users = self.find_users(name)

            if users:

                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(bFrame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20, pady=5,
                                  bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10, padx=3,
                                                              sticky="W")
                            row_no += 1

                Label(bFrame, text="Number of profile\nyou want to block: ", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken", fg="#1877F2").grid(row=row_no+1, column=0, columnspan=2, pady=10, padx=3,
                                                          sticky="W")

                user_to_block = Entry(bFrame, highlightthickness=2)
                user_to_block.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_block.grid(row=row_no+1, column=2, sticky="E")

                b2 = Button(bFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: block_now(int(user_to_block.get()), users, row_no))
                b2.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")

            else:
                Label(bFrame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                    grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(bFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: block.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(bFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    # Unblock another user.
    def unblock_a_user(self):
        unblock = Toplevel()
        unblock.title("Unblock")
        unblock.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        ubFrame = LabelFrame(unblock, text="Unblock a User", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        ubFrame.pack(padx=20, pady=20)

        Label(ubFrame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(ubFrame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def unblock_now(user_ID, users, row_no):
            ID = users[user_ID - 1]
            # Unblocking the user if blocked.
            blocked_user = False
            r = csv.reader(open("Blocked_Users.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][0] == str(self.ID) and lines[lst][1] == ID:
                    blocked_user = True
                    lines.remove(lines[lst])
            writer = csv.writer(open("Blocked_Users.csv", "w", newline=""))
            writer.writerows(lines)
            # If the user wasn't blocked.
            if not blocked_user:
                Label(ubFrame, text="You've not blocked this user.", font=("Roboto", 13), padx=20, pady=5).\
                    grid(row=row_no+3, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(ubFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: unblock.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")
            else:
                Label(ubFrame, text="User unblocked.", font=("Roboto", 13), padx=20, pady=5).\
                    grid(row=row_no+3, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(ubFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: unblock.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")

        def info_entered(name):
            users = self.find_users(name)

            if users:

                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(ubFrame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                      padx=3, sticky="W")
                            row_no += 1

                Label(ubFrame, text="Number of profile\nyou want to unblock: ", font=("Roboto", 13), padx=20, pady=5,
                      bd=1, relief="sunken", fg="#1877F2").grid(row=row_no+1, column=0, columnspan=2, pady=10, padx=3,
                                                                sticky="W")

                user_to_unblock = Entry(ubFrame, highlightthickness=2)
                user_to_unblock.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_unblock.grid(row=row_no+1, column=2, sticky="E")

                b2 = Button(ubFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: unblock_now(int(user_to_unblock.get()), users, row_no))
                b2.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")
            else:
                Label(ubFrame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                    grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(ubFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: unblock.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(ubFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def post(self, post_id):
        personal_page = Toplevel()
        personal_page.title("Make Post")
        personal_page.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        ppFrame = LabelFrame(personal_page, text="Make a Post", font=("Roboto", 15), fg="#1877F2", padx=50,
                             pady=30)
        ppFrame.pack(padx=20, pady=20)

        Label(ppFrame, text="Post From", font=("Roboto", 15), padx=7, relief="groove"). \
            grid(row=0, column=0, columnspan=2, padx=4, pady=7, sticky="W")

        forum = StringVar()
        forum.set("Personal")
        Radiobutton(ppFrame, text="Personal", variable=forum, font=("Helvetica 18 bold", 12),
                    value="1", fg="#1877F2").grid(row=1, column=0, pady=7, sticky="W")
        Radiobutton(ppFrame, text="Page", variable=forum, font=("Helvetica 18 bold", 12),
                    value="0", fg="#1877F2").grid(row=1, column=1, pady=7, sticky="W")

        def post_in_page(page_ID, thepages, row_no):
            rp = csv.reader(open("Posts.csv"))
            linesp = list(rp)
            for lst in range(len(linesp)):
                if linesp[lst][3] == str(post_id):
                    linesp[lst][12] = thepages[int(page_ID) - 1]
                    break
            writer = csv.writer(open("Posts.csv", "w", newline=""))
            writer.writerows(linesp)

            Label(ppFrame, text="Posted.", font=("Roboto", 13), padx=20, pady=5). \
                grid(row=row_no + 3, column=0, columnspan=3, pady=7, sticky="W")
            # Back.
            Button(ppFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: personal_page.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")

        def chosen(choice):
            if choice == str(1):
                Label(ppFrame, text="Posted from account.", font=("Roboto", 15), padx=7, relief="groove"). \
                    grid(row=3, column=0, columnspan=2, padx=4, pady=7, sticky="W")
                # Back.
                Button(ppFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: personal_page.destroy()).grid(row=4, column=0, pady=3, sticky="W")

            elif choice == str(0):

                pages_you_are_in = []
                with open("Page_Members.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[1] == str(self.ID):
                            pages_you_are_in.append(row[0])

                row_no = 2
                your_pages = []
                with open("Pages.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(self.ID) or row[3] in pages_you_are_in:
                            your_pages.append(row[3])
                            Label(ppFrame, text=f"{row[4]}\nCreated by {row[1]} {row[2]} on {row[7]}\nCategory: "
                                                f"{row[5]}", font=("Roboto", 13), padx=20, pady=5, bd=1,
                                  relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                            row_no += 1

                if your_pages:
                    Label(ppFrame, text="Number of page\nyou want to post in: ", font=("Roboto", 13), padx=20, pady=5,
                          bd=1, relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10,
                                                                    padx=3, sticky="W")

                    selected_page = Entry(ppFrame, highlightthickness=2)
                    selected_page.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                    selected_page.grid(row=row_no + 1, column=2, sticky="E")

                    b2 = Button(ppFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                                command=lambda: post_in_page(selected_page.get(), your_pages, row_no))
                    b2.grid(row=row_no + 2, column=0, columnspan=3, pady=7, sticky="W")
                else:
                    Label(ppFrame, text="You've no page.\nPosted from account.", font=("Roboto", 13), padx=20, pady=5).\
                        grid(row=row_no + 3, column=0, columnspan=3, pady=7, sticky="W")
                    # Back.
                    Button(ppFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: personal_page.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")

        Button(ppFrame, text="Enter", font=("Roboto", 12), width=7, fg="#1877F2", command=lambda: chosen(forum.get())).\
            grid(row=2, column=0, columnspan=3, pady=(7, 0), sticky="W")

    # Create a new post.
    def create_a_post(self):

        posting = Toplevel()
        posting.title("Creating Post")
        posting.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        poFrame = LabelFrame(posting, text="Create a New Post", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        poFrame.pack(padx=20, pady=20)

        Label(poFrame, text="Post Type", font=("Roboto", 15), padx=7). \
            grid(row=0, column=0, columnspan=2, padx=4, pady=(7, 0), sticky="W")
        Label(poFrame, text="Post Title", font=("Roboto", 15), padx=7). \
            grid(row=2, column=0, columnspan=2, padx=4, pady=7, sticky="W")
        Label(poFrame, text="Post Description", font=("Roboto", 15), padx=7). \
            grid(row=3, column=0, columnspan=2, padx=4, pady=7, sticky="W")
        Label(poFrame, text="File Path", font=("Roboto", 15), padx=7). \
            grid(row=5, column=0, columnspan=2, padx=4, pady=7, sticky="W")

        title = Entry(poFrame, highlightthickness=2)
        title.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        description = Entry(poFrame, highlightthickness=2)
        description.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        path = Entry(poFrame, highlightthickness=2)
        path.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

        ptype = StringVar()
        ptype.set("Image")
        Radiobutton(poFrame, text="Image", variable=ptype, font=("Helvetica 18 bold", 12),
                    value="Image", fg="#1877F2").grid(row=1, column=0, pady=7, sticky="W")
        Radiobutton(poFrame, text="Video", variable=ptype, font=("Helvetica 18 bold", 12),
                    value="Video", fg="#1877F2").grid(row=1, column=1, pady=7, sticky="W")

        title.grid(row=2, column=2, pady=7, sticky="E")
        description.grid(row=3, column=2, pady=7, sticky="E")
        path.grid(row=5, column=2, pady=7, sticky="E")

        def upload_file():
            poFrame.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Saifia\PycharmProjects\MyProjects\
            ooppython\Images", title="Select a File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
            path.insert(0, poFrame.filename)

        Button(poFrame, text="Upload", font=("Roboto", 12), width=7, fg="#1877F2", command=upload_file). \
            grid(row=4, column=0, columnspan=3, pady=(7,0), sticky="W")

        l2 = Label(poFrame, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                   padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

        def create_now():
            global l2_info

            if title.index("end") == 0 or description.index("end") == 0 or path.index("end") == 0:
                l2.grid(row=7, column=0, columnspan=2, pady=5, padx=3, sticky="W")
                l2_info = l2.grid_info()
            else:
                if l2_info != {}:
                    if l2_info["row"] == 7:
                        l2.destroy()

                post_obj = Post()

                post_obj.post_type = ptype.get()
                post_obj.post_title = title.get()
                post_obj.post_description = description.get()
                post_obj.file_path = path.get()
                post_obj.post_time = datetime.datetime.now().time().replace(microsecond=0)
                post_obj.post_date = datetime.datetime.now().date()

                # Each post gets a unique post id.
                r = csv.reader(open("Posts.csv"))
                lines = list(r)
                for lst in range(1, len(lines)):
                    if lines[lst][3]:
                        Post.post_id = lines[lst][3]

                post_obj.post_id = int(Post.post_id) + 1

                with open("Friends.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(self.ID) or row[3] == str(self.ID):
                            post_obj.post_recipients += 1

                # Adding user's post to database.
                with open("Posts.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow([self.ID, self.first_name, self.last_name, post_obj.post_id, post_obj.post_type,
                                         post_obj.post_title, post_obj.post_description, post_obj.post_time,
                                         post_obj.post_date, post_obj.privacy_id, post_obj.post_notification,
                                         post_obj.post_recipients, post_obj.page_id, post_obj.file_path])
                self.post(post_obj.post_id)

        Button(poFrame, text="Done", font=("Roboto", 14), width=9, bg="#1877F2", fg="white", command=create_now). \
            grid(row=6, column=0, columnspan=3, pady=7, sticky="W")

    # View comments on a post.
    @staticmethod
    def view_comments(chosen_post_id):
        comment_count = 0
        with open("Comments.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[1] == chosen_post_id:
                    comment_count += 1
                    print(f"{row[2]}")
        print(f"{comment_count} comment(s).")

    # Search through posts for a word.
    @staticmethod
    def search_posts(ID, word):
        with open("Posts.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == ID and word in row[5] or row[0] == ID and word in row[6]:
                    print(f"Post Type: {row[4]}\nPost Title: {row[5]}\nPost Description: {row[6]}\nPost Time: "
                          f"{row[7]}\nPost Date: {row[8]}\n")
        print("\nPosts containing the given word.")

    # Add a friend.
    def add_friend(self):
        adding = Toplevel()
        adding.title("Add Friend")
        adding.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        afFrame = LabelFrame(adding, text="Message a User", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        afFrame.pack(padx=15, pady=15)

        Label(afFrame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(afFrame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def send_request(user_ID, users, row_no):

            friend_ID = users[int(user_ID)-1]

            already_friends = False
            with open("Friends.csv") as friend_file:
                csv_reader = csv.reader(friend_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID) and row[3] == friend_ID and row[6] == str(False) or row[0] == friend_ID \
                            and row[3] == str(self.ID) and row[6] == str(False):
                        already_friends = True
                        break

            if not already_friends:

                request_pending = False
                with open("Friends.csv") as friend_file:
                    csv_reader = csv.reader(friend_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(self.ID) and row[3] == friend_ID and row[6] == str(True):
                            request_pending = True
                            break

                if request_pending:
                    Label(afFrame, text="Friend request pending.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                          relief="groove").grid(row=row_no + 3, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                    # Back.
                    Button(afFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: adding.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")
                else:
                    user_friend = Friend()
                    with open("Friends.csv", "a", newline="") as data_file:
                        csv_writer = csv.writer(data_file, delimiter=",")
                        csv_writer.writerow([self.ID, self.first_name, self.last_name, friend_ID,
                                             user_friend.first_name, user_friend.last_name, user_friend.pending])

                    Label(afFrame, text="Friend request sent.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                          relief="groove").grid(row=row_no + 3, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                    # Back.
                    Button(afFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: adding.destroy()).grid(row=row_no+4, column=0, pady=3, sticky="W")
            else:
                Label(afFrame, text="You're already friends.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="groove").grid(row=row_no + 3, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                # Back.
                Button(afFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: adding.destroy()).grid(row=row_no+4, column=0, pady=3, sticky="W")

        def info_entered(user_name):
            users = self.find_users(user_name)

            if users:
                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(afFrame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                      padx=3, sticky="W")
                            row_no += 1

                Label(afFrame, text="Number of profile\nyou want to befriend: ", font=("Roboto", 13), padx=20, pady=5,
                      bd=1, relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10, padx=3,
                                                                sticky="W")

                user_to_friend = Entry(afFrame, highlightthickness=2)
                user_to_friend.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_friend.grid(row=row_no + 1, column=2, sticky="E")

                b2 = Button(afFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: send_request(int(user_to_friend.get()), users, row_no))
                b2.grid(row=row_no + 2, column=0, columnspan=3, pady=7, sticky="W")
            else:
                Label(afFrame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                    grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(afFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: adding.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(afFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    # Send message to another user.
    def send_message(self):
        messaging = Toplevel()
        messaging.title("Send Message")
        messaging.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        smFrame = LabelFrame(messaging, text="Message a User", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        smFrame.pack(padx=15, pady=15)

        Label(smFrame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(smFrame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def send_now(ID, users, row_no, message_to_send):
            Label(smFrame, text="Message sent.", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="groove"). \
                grid(row=row_no + 6, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            message_input = message_to_send
            user_ID = users[int(ID)-1]

            # Creating message object.
            message = Message()
            # Setting attributes.
            message.receiver_ID, message.sender_ID = user_ID, self.ID
            message.sender_first_name, message.sender_last_name = self.first_name, self.last_name
            message.content = message_input
            # Storing message data into a csv file.
            with open("Message.csv", "a", newline="") as data_file:
                csv_writer = csv.writer(data_file, delimiter=",")
                csv_writer.writerow([message.receiver_ID, message.sender_ID, message.sender_first_name,
                                     message.sender_last_name, message.content, message.pending])

        def type_message(user_ID, users, row_no):
            Label(smFrame, text="Enter Message", font=("Roboto", 13), padx=15, pady=5, bd=1, relief="sunken"). \
                grid(row=row_no+3, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            message_content = Entry(smFrame, highlightthickness=2)
            message_content.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            message_content.grid(row=row_no+3, column=2, sticky="E")

            b3 = Button(smFrame, text="Send", font=("Roboto", 13), width=7, fg="#1877F2",
                        command=lambda: send_now(user_ID, users, row_no, message_content.get()))
            b3.grid(row=row_no+5, column=0, columnspan=3, pady=7, sticky="W")

        def info_entered(user_name):
            users = self.find_users(user_name)

            if users:
                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(smFrame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                      padx=3, sticky="W")
                            row_no += 1

                Label(smFrame, text="Number of profile\nyou want to message: ", font=("Roboto", 13), padx=20, pady=5,
                      bd=1, relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10,
                                                                padx=3, sticky="W")

                user_to_message = Entry(smFrame, highlightthickness=2)
                user_to_message.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_message.grid(row=row_no + 1, column=2, sticky="E")

                b2 = Button(smFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: type_message(int(user_to_message.get()), users, row_no))
                b2.grid(row=row_no + 2, column=0, columnspan=3, pady=7, sticky="W")
            else:
                Label(smFrame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                    grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(smFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: messaging.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(smFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def notifications(self):

        notify = Toplevel()
        notify.title("Notifications")
        notify.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        npFrame = LabelFrame(notify, text="Post Notification", font=("Roboto", 15), fg="#1877F2", padx=40, pady=20)
        npFrame.grid(row=0, column=0, sticky="W", pady=15, padx=15)

        nmFrame = LabelFrame(notify, text="Message Notification", font=("Roboto", 15), fg="#1877F2", padx=40,
                             pady=20)
        nmFrame.grid(row=1, column=0, sticky="W", pady=15, padx=15)

        cnFrame = LabelFrame(notify, text="Comment Notification", font=("Roboto", 15), fg="#1877F2", padx=40,
                             pady=20)
        cnFrame.grid(row=2, column=0, sticky="W", pady=15, padx=15)

        # Post notifications.
        user_friends = []

        with open("Friends.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID) and row[6] == str(False):
                    user_friends.append(row[3])
                elif row[3] == str(self.ID) and row[6] == str(False):
                    user_friends.append(row[0])

        print(user_friends)

        with open("Posts.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] in user_friends and str(row[10]) != str(row[11]):
                    print(f"One of your friends {row[1]} {row[2]} posted.")
                    Label(npFrame, text=f"One of your friends\n{row[1]} {row[2]} posted.", font=("Roboto", 13), padx=20,
                          pady=5, bd=1, relief="groove").grid(row=0, column=0, columnspan=2, pady=10,
                                                              padx=3, sticky="W")

                    friend_user_id = row[0]
                    notification_count = int(row[10]) + 1

                    r = csv.reader(open("Posts.csv"))
                    lines = list(r)
                    for lst in range(len(lines)):
                        if lines[lst][0] == friend_user_id:
                            lines[lst][10] = notification_count
                            break
                    writer = csv.writer(open("Posts.csv", "w", newline=""))
                    writer.writerows(lines)

                    break
                else:
                    Label(npFrame, text=f"None of your friends\nposted recently.", font=("Roboto", 13), padx=20,
                          pady=5, bd=1, relief="groove").grid(row=0, column=0, columnspan=2, pady=10,
                                                              padx=3, sticky="W")
        # Message Notification.

        with open("Message.csv") as friend_file:
            csv_reader = csv.reader(friend_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID) and row[5] == str(True):
                    Label(nmFrame, text=f"You've a new message from {row[2]} {row[3]}.", font=("Roboto", 13), padx=20,
                          pady=5, bd=1, relief="groove").grid(row=0, column=0, columnspan=2, pady=5, padx=3,
                                                              sticky="W")
                    Label(nmFrame, text=f"'{row[4]}'", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="groove",
                          fg="#1877F2").grid(row=0, column=2, pady=5, padx=3, sticky="W")
                    break
                else:
                    Label(nmFrame, text="No new messages.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                          relief="groove").grid(row=0, column=0, columnspan=2, pady=5, padx=3, sticky="W")
            # Clearing the queue.
        r = csv.reader(open("Message.csv"))
        lines = list(r)
        for lst in range(len(lines)):
            if lines[lst][0] == str(self.ID) and lines[lst][5] == str(True):
                lines[lst][5] = False
                break
        writer = csv.writer(open("Message.csv", "w", newline=""))
        writer.writerows(lines)

        # Comment Notification.

        with open("Comments.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID) and row[6] == str(True):
                    Label(cnFrame, text=f"You've a new comment from {row[4]} {row[5]}.", font=("Roboto", 13), padx=20,
                          pady=5, bd=1, relief="groove").grid(row=0, column=0, columnspan=2, pady=5, padx=3, sticky="W")
                    Label(cnFrame, text=f"'{row[2]}'", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="groove",
                          fg="#1877F2").grid(row=0, column=2, pady=5, padx=3, sticky="E")
                    break
            else:
                Label(cnFrame, text="No new comments.", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="groove").\
                    grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")
        # Clearing the queue.
        r = csv.reader(open("Comments.csv"))
        lines = list(r)
        for lst in range(len(lines)):
            if lines[lst][0] == str(self.ID) and lines[lst][6] == str(True):
                lines[lst][6] = False
                break
        writer = csv.writer(open("Comments.csv", "w", newline=""))
        writer.writerows(lines)

    # Create a privacy list and add friends in it.
    def create_privacy_list(self):
        global private_friends
        global pl1
        global friend_to_add
        private_friends.clear()
        privacy_list = Toplevel()
        privacy_list.title("Create Privacy List")
        privacy_list.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        plFrame = LabelFrame(privacy_list, text="Create a Private List", font=("Roboto", 15), fg="#1877F2", padx=50,
                             pady=30)
        plFrame.pack(padx=15, pady=15)

        your_friends = []
        # Finding all users with the first name that you searched for.
        with open("Friends.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID) and row[6] == str(False):
                    your_friends.append(row[3])
                elif row[3] == str(self.ID) and row[6] == str(False):
                    your_friends.append(row[0])

        r = csv.reader(open("Privacy_lists.csv"))
        lines = list(r)
        for lst in range(1, len(lines)):
            if lines[lst][0]:
                User.privacy_lst_id = lines[lst][0]
        lst_id = int(User.privacy_lst_id) + 1

        def write_onto_csv(chosen_friends, row_no):
            with open("Privacy_lists.csv", "a", newline="") as data_file:
                csv_writer = csv.writer(data_file, delimiter=",")
                csv_writer.writerow([lst_id, chosen_friends])
            Label(plFrame, text="Friends added to list.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                  relief="sunken").grid(row=row_no + 6, column=0, columnspan=3, pady=7, sticky="W")
            # Back.
            Button(plFrame, text="Back", font=("Roboto", 13), width=8, fg="#1877F2",
                   command=lambda: privacy_list.destroy()).grid(row=row_no + 7, column=0, columnspan=3, pady=7,
                                                                sticky="W")

        def just_add_now(friend, yp_friends, row_no):
            global private_friends
            global pl1
            global friend_to_add
            private_friends.append(yp_friends[int(friend)-1])
            pl1.grid_forget()
            friend_to_add.grid_forget()
            add_now(your_friends, row_no)

        def add_now(yp1_friends, row_no):
            global private_friends
            global pl1
            global friend_to_add
            pl1 = Label(plFrame, text="Number of friend\nyou want to add: ", font=("Roboto", 13), padx=4, pady=5, bd=1,
                        relief="sunken")
            pl1.grid(row=row_no + 2, column=0, columnspan=2, pady=(7,4), padx=3, sticky="W")

            friend_to_add = Entry(plFrame, highlightthickness=2)
            friend_to_add.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            friend_to_add.grid(row=row_no + 2, column=2, sticky="E")

            plb3 = Button(plFrame, text="Enter", font=("Roboto", 13), width=7,
                          command=lambda: just_add_now(friend_to_add.get(), yp1_friends, row_no))
            plb3.grid(row=row_no + 4, column=0, columnspan=3, pady=(4,7), sticky="W")

            plb3 = Button(plFrame, text="Done", font=("Roboto", 13), width=8, bg="#1877F2", fg="white",
                          command=lambda: write_onto_csv(private_friends, row_no))
            plb3.grid(row=row_no + 5, column=0, columnspan=3, pady=7, sticky="W")

        def see_your_friends(your_friends):
            if your_friends:

                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in your_friends:
                            Label(plFrame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                      padx=3, sticky="W")
                            row_no += 1

                plb2 = Button(plFrame, text="Add", font=("Roboto", 13), width=7, fg="#1877F2",
                              command=lambda: add_now(your_friends, row_no))
                plb2.grid(row=row_no + 1, column=0, columnspan=3, pady=7, sticky="W")

            else:
                Label(plFrame, text="You've no friends to add.", font=("Roboto", 14), padx=20, pady=5, bd=1,
                      relief="sunken").grid(row=2, column=0, columnspan=2, pady=10, padx=3,
                                                          sticky="W")

        Label(plFrame, text=f"A private list has been created with id {lst_id}.", font=("Roboto", 14), padx=20, pady=5,
              bd=1, relief="sunken").grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")
        Label(plFrame, text=f"Add friends to it.", font=("Roboto", 14), padx=20, pady=5, bd=1, relief="sunken").\
            grid(row=1, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        plb1 = Button(plFrame, text="See Friends", font=("Roboto", 13), width=12, fg="#1877F2",
                      command=lambda: see_your_friends(your_friends))
        plb1.grid(row=2, column=0, columnspan=2, pady=10, padx=3, sticky="W")

    # Link a post with any privacy list.
    def make_a_post_private(self):
        post_privacy = Toplevel()
        post_privacy.title("Post Privacy")
        post_privacy.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        popFrame = LabelFrame(post_privacy, text="Make Post Private", font=("Roboto", 15), fg="#1877F2", padx=50,
                             pady=30)
        popFrame.pack(padx=15, pady=15)

        Label(popFrame, text="Your posts: ", font=("Roboto", 14), padx=5, pady=5, bd=1, relief="sunken",
              fg="#1877F2").grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        global post_to_add
        global private_lst

        l4 = Label(popFrame, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                   padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

        def add_post_now(postID, posts_lst, lst_id, row_no):
            global l4_info
            global post_to_add
            global private_lst

            if post_to_add.index("end") == 0 or private_lst.index("end") == 0:
                l4.grid(row=row_no+4, column=0, columnspan=2, pady=5, padx=3, sticky="W")
                l4_info = l4.grid_info()
            else:
                if l4_info != {}:
                    if l4_info["row"] == row_no+4:
                        l4.destroy()
                private_post_id = posts_lst[int(postID) - 1]
                r = csv.reader(open("Posts.csv"))
                lines = list(r)
                for lst in range(len(lines)):
                    if lines[lst][3] == private_post_id:
                        lines[lst][9] = lst_id
                        break
                writer = csv.writer(open("Posts.csv", "w", newline=""))
                writer.writerows(lines)

                Label(popFrame, text="Post made private.", font=("Roboto", 14), padx=20, pady=5, relief="groove"). \
                    grid(row=row_no+4, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(popFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: post_privacy.destroy()).grid(row=row_no+5, column=0, pady=3, sticky="W")

        posts = self.view_user_posts()

        if posts:
            row_no = 1

            with open("Posts.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == self.ID and not row[12]:
                        Label(popFrame, text=f"Post Title: {row[5]}\nPost Description: {row[6]}", font=("Roboto", 13),
                              padx=20, pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                           padx=3, sticky="W")
                        row_no += 1

            Label(popFrame, text="Number of post\nyou want to add: ", font=("Roboto", 13), padx=20, pady=5,
                  bd=1, relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10,
                                                            padx=3, sticky="W")

            post_to_add = Entry(popFrame, highlightthickness=2)
            post_to_add.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            post_to_add.grid(row=row_no + 1, column=2, sticky="E")

            Label(popFrame, text="Privacy list ID: ", font=("Roboto", 13), padx=20, pady=5,
                  bd=1, relief="sunken", fg="#1877F2").grid(row=row_no + 2, column=0, columnspan=2, pady=10,
                                                            padx=3, sticky="W")

            private_lst = Entry(popFrame, highlightthickness=2)
            private_lst.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            private_lst.grid(row=row_no + 2, column=2, sticky="E")

            b2 = Button(popFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                        command=lambda: add_post_now(post_to_add.get(), posts, private_lst.get(), row_no))
            b2.grid(row=row_no + 3, column=0, columnspan=3, pady=7, sticky="W")

        else:
            Label(popFrame, text="You've no posts.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
            # Back.
            Button(popFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: post_privacy.destroy()).grid(row=3, column=0, pady=3, sticky="W")

    # Creating a Facebook Page.
    def create_a_page(self):

        paging = Toplevel()
        paging.title("Creating Page")
        paging.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        pgFrame = LabelFrame(paging, text="Create a New Page", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        pgFrame.pack(padx=20, pady=20)

        Label(pgFrame, text="Page Name", font=("Roboto", 15), padx=7). \
            grid(row=0, column=0, columnspan=2, padx=4, pady=(7, 0), sticky="W")
        Label(pgFrame, text="Page Category", font=("Roboto", 15), padx=7). \
            grid(row=2, column=0, columnspan=2, padx=4, pady=7, sticky="W")
        Label(pgFrame, text="Page Description", font=("Roboto", 15), padx=7). \
            grid(row=7, column=0, columnspan=2, padx=4, pady=7, sticky="W")

        pgname = Entry(pgFrame, highlightthickness=2)
        pgname.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        pgdescription = Entry(pgFrame, highlightthickness=2)
        pgdescription.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

        pgcat = StringVar()
        pgcat.set("Local Business or Place")
        Radiobutton(pgFrame, text="Local Business or Place", variable=pgcat, font=("Helvetica 18 bold", 12),
                    value="Local Business or Place", fg="#1877F2").grid(row=3, column=0, pady=4, sticky="W")
        Radiobutton(pgFrame, text="Brand or Product", variable=pgcat, font=("Helvetica 18 bold", 12),
                    value="Brand or Product", fg="#1877F2").grid(row=4, column=0, pady=4, sticky="W")
        Radiobutton(pgFrame, text="Artist or Public Figure", variable=pgcat, font=("Helvetica 18 bold", 12),
                    value="Artist or Public Figure", fg="#1877F2").grid(row=5, column=0, pady=4, sticky="W")
        Radiobutton(pgFrame, text="Entertainment", variable=pgcat, font=("Helvetica 18 bold", 12),
                    value="Entertainment", fg="#1877F2").grid(row=6, column=0, pady=4, sticky="W")

        pgname.grid(row=0, column=2, pady=7, sticky="E")
        pgdescription.grid(row=7, column=2, pady=7, sticky="E")

        l3 = Label(pgFrame, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                   padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

        def create_now():
            global l3_info

            if pgname.index("end") == 0 or pgdescription.index("end") == 0:
                l3.grid(row=9, column=0, columnspan=2, pady=5, padx=3, sticky="W")
                l3_info = l3.grid_info()
            else:
                if l3_info != {}:
                    if l3_info["row"] == 9:
                        l3.destroy()

                page_obj = Page()

                page_obj.name = pgname.get()
                page_obj.category = pgcat.get()
                page_obj.description = pgdescription.get()
                page_obj.creation_date = datetime.datetime.now().date()

                # Each page gets a unique page id.
                r = csv.reader(open("Pages.csv"))
                lines = list(r)
                for lst in range(1, len(lines)):
                    if lines[lst][3]:
                        Page.page_id = lines[lst][3]

                page_obj.page_id = int(Page.page_id) + 1

                # Adding user's page to database.
                with open("Pages.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow([self.ID, self.first_name, self.last_name, page_obj.page_id, page_obj.name,
                                         page_obj.category, page_obj.description, page_obj.creation_date])
                # Page Created.
                Label(pgFrame, text="Page Created.", font=("Helvetica 18 bold", 14), padx=18, pady=4, bd=1,
                      relief="groove").grid(row=9, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(pgFrame, text="Back", font=("Roboto", 14), width=9, fg="#1877F2",
                       command=lambda: paging.destroy()).grid(row=10, column=0, columnspan=3, pady=7, sticky="W")

        Button(pgFrame, text="Done", font=("Roboto", 14), width=9, bg="#1877F2", fg="white", command=create_now). \
            grid(row=8, column=0, columnspan=3, pady=7, sticky="W")

    @staticmethod
    def find_pages(name):
        pages = []
        with open("Pages.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[4] == name:
                    pages.append(row[3])
        return pages

    def display_page(self, page_ID):

        displaying_page = Toplevel()
        displaying_page.title("See Page")
        displaying_page.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        dpiFrame = LabelFrame(displaying_page, text="Page Info", font=("Roboto", 15), fg="#1877F2", padx=20,
                              pady=10)
        dpiFrame.grid(row=0, column=0, padx=20, pady=(15, 4), sticky="W")

        lpFrame = LabelFrame(displaying_page, text="Like Page", font=("Roboto", 15), fg="#1877F2", padx=20,
                             pady=10)
        lpFrame.grid(row=1, column=1, padx=20, pady=(15, 4), sticky="W")

        dppFrame = LabelFrame(displaying_page, text="Page Posts", font=("Roboto", 15), fg="#1877F2", padx=20,
                              pady=10)
        dppFrame.grid(row=1, column=0, padx=10, pady=(4, 15), sticky="W")

        def like_page_now(page_to_like_ID):

            global lpb

            already_liked = False
            with open("Page_Members.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == page_to_like_ID and row[1] == str(self.ID):
                        already_liked = True
                        break

            owner = False
            with open("Pages.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID) and row[3] == page_to_like_ID:
                        owner = True
                        break

            if owner:
                lpb = Button(lpFrame, text="Like Page", width=12, font=("Roboto", 14), relief="raised",
                             state="disabled")
                Label(lpFrame, text="You created page.", font=("Roboto", 14), relief="groove"). \
                    grid(row=1, column=0, pady=3, sticky="W")
            elif not already_liked:
                with open("Page_Members.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow([page_to_like_ID, self.ID])
                lpb = Button(lpFrame, text="Like Page", width=12, font=("Roboto", 14), relief="raised",
                             state="disabled")
                Label(lpFrame, text="Page Liked.", font=("Roboto", 14), relief="groove").\
                    grid(row=1, column=0, pady=3, sticky="W")
            else:
                lpb = Button(lpFrame, text="Like Page", width=12, font=("Roboto", 14), relief="raised",
                             state="disabled")
                Label(lpFrame, text="Page already liked.", font=("Roboto", 14), relief="groove").\
                    grid(row=1, column=0, pady=3, sticky="W")

        lpb = Button(lpFrame, text="Like Page", width=12, font=("Roboto", 14), relief="raised",
                     command=lambda: like_page_now(page_ID))
        lpb.grid(row=0, column=0, sticky="W")

        with open("Pages.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[3] == page_ID:
                    name = row[4]
                    creator_first = row[1]
                    creator_last = row[2]
                    category = row[5]
                    page_des = row[6]
                    created_date = row[7]

        Label(dpiFrame, text="Name:", font=("Roboto", 13)).grid(row=1, column=0, pady=3, sticky="W")
        Label(dpiFrame, text=name, font=("Helvetica", 13)).grid(row=1, column=1, pady=3, sticky="W")
        Label(dpiFrame, text="Created By: ", font=("Roboto", 13)).grid(row=2, column=0, pady=3, sticky="W")
        Label(dpiFrame, text=creator_first + "" + creator_last, font=("Helvetica", 13)).grid(row=2, column=1, pady=3,
                                                                                             sticky="W")
        Label(dpiFrame, text="Created On: ", font=("Roboto", 13)).grid(row=3, column=0, pady=3, sticky="W")
        Label(dpiFrame, text=created_date, font=("Helvetica", 13)).grid(row=3, column=1, pady=3, sticky="W")
        Label(dpiFrame, text="Category: ", font=("Roboto", 13)).grid(row=4, column=0, pady=3, sticky="W")
        Label(dpiFrame, text=category, font=("Helvetica", 13)).grid(row=4, column=1, pady=3, sticky="W")
        Label(dpiFrame, text="Description: ", font=("Roboto", 13)).grid(row=5, column=0, pady=3, sticky="W")
        Label(dpiFrame, text=page_des, font=("Helvetica", 13)).grid(row=5, column=1, pady=3, sticky="W")

        pstitle1 = []
        psdescription1 = []
        psPostid = []
        psUserid = []
        psfirst = []
        pslast = []
        global psfilepath1
        global psImage1
        global images1
        global title_label1
        global image_label1
        global description_label1
        global button_forward1
        global button_back1
        global button_comment
        global name_label
        images1.clear()
        psfilepath1.clear()
        post_num = 1

        has_posts = False
        with open("Posts.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[12] == page_ID:
                    psfirst.append(row[1])
                    pslast.append(row[2])
                    psUserid.append(row[0])
                    psPostid.append(row[3])
                    pstitle1.append(row[5])
                    psdescription1.append(row[6])
                    psfilepath1.append(row[13])
                    has_posts = True

        if has_posts:
            for pic in psfilepath1:
                my_pic = Image.open(pic)
                resized = my_pic.resize((320, 220))
                new_pic = ImageTk.PhotoImage(resized)
                images1.append(new_pic)

            title_label1 = Label(dppFrame, text=pstitle1[post_num - 1], font=("Roboto", 13), padx=7,
                                 pady=5)
            image_label1 = Label(dppFrame, image=images1[post_num - 1])
            description_label1 = Label(dppFrame, text=psdescription1[post_num - 1],
                                       font=("Helvetica bold 18", 13), padx=7, pady=3)
            name_label = Label(dppFrame, text="Posted by " + psfirst[post_num - 1] + " " + pslast[post_num-1],
                               font=("Roboto", 13), padx=7, pady=3)

            def forward(p_num):
                global title_label1
                global image_label1
                global description_label1
                global button_forward1
                global button_back1
                global button_comment
                global name_label
                global images1

                title_label1.grid_forget()
                image_label1.grid_forget()
                description_label2.grid_forget()

                title_label1 = Label(dppFrame, text=pstitle1[p_num - 1], font=("Roboto", 13), padx=7,
                                     pady=5)
                image_label1 = Label(dppFrame, image=images1[p_num - 1])
                description_label1 = Label(dppFrame, text=psdescription1[p_num - 1],
                                           font=("Helvetica bold 18", 13), padx=7, pady=3)
                name_label = Label(dppFrame, text="Posted by " + psfirst[p_num - 1] + " " + pslast[p_num - 1],
                                   font=("Roboto", 13), padx=7, pady=3)

                button_forward1 = Button(dppFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                         command=lambda: forward(p_num + 1))
                button_back1 = Button(dppFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                      command=lambda: back(p_num - 1))
                button_comment = Button(dppFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                        command=lambda: Post.comment_on_a_post(psPostid[p_num - 1],
                                                                               psUserid[p_num - 1], self))

                if p_num == len(images1):
                    button_forward1 = Button(dppFrame, text=">>", width=6, font=("Roboto", 13),
                                             state="disabled")

                title_label1.grid(row=0, column=0, sticky="W")
                image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                description_label1.grid(row=2, column=0, sticky="W", pady=7)
                button_forward1.place(x=250, y=300)
                button_comment.place(x=100, y=300)
                button_back1.grid(row=3, column=0, sticky="W")
                name_label.grid(row=4, column=0, sticky="W")

            def back(p_num):
                global title_label1
                global image_label1
                global description_label1
                global button_forward1
                global button_back1
                global name_label
                global button_comment
                global images1

                title_label1.grid_forget()
                image_label1.grid_forget()
                description_label1.grid_forget()

                title_label1 = Label(dppFrame, text=pstitle1[p_num - 1], font=("Roboto", 13), padx=7,
                                     pady=5)
                image_label1 = Label(dppFrame, image=images1[p_num - 1])
                description_label1 = Label(dppFrame, text=psdescription1[p_num - 1],
                                           font=("Helvetica bold 18", 13), padx=7, pady=3)
                name_label = Label(dppFrame, text="Posted by " + psfirst[p_num - 1] + " " + pslast[p_num - 1],
                                   font=("Roboto", 13), padx=7, pady=3)

                button_forward1 = Button(dppFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                         command=lambda: forward(p_num + 1))
                button_back1 = Button(dppFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                      command=lambda: back(p_num - 1))
                button_comment = Button(dppFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                        command=lambda: Post.comment_on_a_post(psPostid[p_num - 1], psUserid[p_num - 1],
                                                                               self))

                if p_num == 1:
                    button_back1 = Button(dppFrame, text="<<", width=6, font=("Roboto", 13),
                                          state="disabled")

                title_label1.grid(row=0, column=0, sticky="W")
                image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                description_label1.grid(row=2, column=0, sticky="W", pady=7)
                button_forward1.place(x=250, y=300)
                button_comment.place(x=100, y=300)
                button_back1.grid(row=3, column=0, sticky="W")
                name_label.grid(row=4, column=0, sticky="W")

            if len(images1) != 1:
                button_forward1 = Button(dppFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                         command=lambda: forward(post_num + 1))
                button_back1 = Button(dppFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                      command=lambda: back(post_num))
            else:
                button_forward1 = Button(dppFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                         state="disabled")
                button_back1 = Button(dppFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2", state="disabled")

            button_comment = Button(dppFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                    command=lambda: Post.comment_on_a_post(psPostid[post_num - 1],
                                                                           psUserid[post_num - 1], self))

            title_label1.grid(row=0, column=0, sticky="W")
            image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
            description_label1.grid(row=2, column=0, sticky="W", pady=7)
            button_forward1.place(x=250, y=300)
            button_comment.place(x=100, y=300)
            button_back1.grid(row=3, column=0, sticky="W")
            name_label.grid(row=4, column=0, sticky="W")

        if not has_posts:
            Label(dppFrame, text="Page has no posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3, sticky="W")

    def search_page(self):
        search_page_win = Toplevel()
        search_page_win.title("Search Page")
        search_page_win.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        spFrame = LabelFrame(search_page_win, text="Search a Page", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        spFrame.pack(padx=20, pady=20)

        Label(spFrame, text="Page Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        page_name = Entry(spFrame, highlightthickness=2)
        page_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        page_name.grid(row=0, column=2, sticky="E")

        def search_now(ID, pages_found):
            page_ID = pages_found[ID - 1]
            # Destroying the search window and displaying the page.
            search_page_win.destroy()
            self.display_page(page_ID)

        def info_entered(name):
            pages_to_find = self.find_pages(name)

            if pages_to_find:
                row_no = 2

                with open("Pages.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[4] == name:
                            Label(spFrame, text=f"{row[4]}\nCreated By: {row[1]} {row[2]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10, padx=3,
                                                                      sticky="W")
                            row_no += 1

                Label(spFrame, text="Number of page\nyou want to see: ", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10, padx=3,
                                                          sticky="W")

                page_to_see = Entry(spFrame, highlightthickness=2)
                page_to_see.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                page_to_see.grid(row=row_no + 1, column=2, sticky="E")

                b2 = Button(spFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: search_now(int(page_to_see.get()), pages_to_find))
                b2.grid(row=row_no + 2, column=0, columnspan=3, pady=7, sticky="W")
            else:
                Label(spFrame, text="Page not found.", font=("Roboto", 14), padx=20, pady=5, bd=1, relief="sunken"). \
                    grid(row=2, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                # Back.
                Button(spFrame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: search_page_win.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(spFrame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(page_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def like_a_page(self, page_id):
        pass

    def display_user_profile(self, ID):
        displaying = Toplevel()
        displaying.title("See User")
        displaying.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        piFrame = LabelFrame(displaying, text="Profile Info.", font=("Roboto", 15), fg="#1877F2", padx=40, pady=20)
        piFrame.grid(row=0, column=0, sticky="W", padx=15, pady=(10, 5))

        upFrame = LabelFrame(displaying, text="Posts", font=("Roboto", 15), fg="#1877F2", padx=40, pady=20)
        upFrame.grid(row=1, column=0, sticky="W", padx=15, pady=(5, 10))

        pstitle1 = []
        psdescription1 = []
        psPostid = []
        global psfilepath1
        global psImage1
        global images1
        global title_label1
        global image_label1
        global description_label1
        global button_forward1
        global button_back1
        global button_comment
        global private_title
        global private_description
        global private_filepath
        images1.clear()
        psfilepath1.clear()

        private_account = False
        with open("Users_Database.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == ID:
                    Label(piFrame, text=f"{row[1]} {row[2]}", font=("Roboto", 12)).\
                        grid(row=0, column=0, pady=3, sticky="W")
                    about = row[7]
                    current_city = row[8]
                    Education = row[9]
                    Workplace = row[10]
                    Status = row[11]
                if row[0] == ID and row[12] == str(True):
                    private_account = True

        Label(piFrame, text="About:", font=("Roboto", 12)).grid(row=1, column=0, pady=3, sticky="W")
        Label(piFrame, text=about, font=("Helvetica", 12)).grid(row=1, column=1, pady=3, sticky="W")
        Label(piFrame, text="Current City: ", font=("Roboto", 12)).grid(row=2, column=0, pady=3, sticky="W")
        Label(piFrame, text=current_city, font=("Helvetica", 12)).grid(row=2, column=1, pady=3, sticky="W")
        Label(piFrame, text="Education: ", font=("Roboto", 12)).grid(row=3, column=0, pady=3, sticky="W")
        Label(piFrame, text=Education, font=("Helvetica", 12)).grid(row=3, column=1, pady=3, sticky="W")
        Label(piFrame, text="Workplace: ", font=("Roboto", 12)).grid(row=4, column=0, pady=3, sticky="W")
        Label(piFrame, text=Workplace, font=("Helvetica", 12)).grid(row=4, column=1, pady=3, sticky="W")
        Label(piFrame, text="Relationship Status: ", font=("Roboto", 12)).grid(row=5, column=0, pady=3, sticky="W")
        Label(piFrame, text=Status, font=("Helvetica", 12)).grid(row=5, column=1, pady=3, sticky="W")

        # If that user's account is public.
        if not private_account:
            # Display Posts.
            post_num = 1

            has_posts = False
            with open("Posts.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(ID) and row[9] == str(0) and not row[12]:
                        psPostid.append(row[3])
                        pstitle1.append(row[5])
                        psdescription1.append(row[6])
                        psfilepath1.append(row[13])
                        has_posts = True
                    if row[0] == str(ID) and row[9] != str(0) and not row[12]:
                        has_posts = True
                        access_to_private_post = False
                        post_privacy_id = row[9]
                        # Checking if you've access to that private post.
                        with open("Privacy_lists.csv") as private_lst_file:
                            csv_reader = csv.reader(private_lst_file, delimiter=",")
                            for line in csv_reader:
                                if line[0] == post_privacy_id and str(self.ID) in line[1]:
                                    access_to_private_post = True
                                    break
                        if access_to_private_post:
                            psPostid.append(row[3])
                            pstitle1.append(row[5])
                            psdescription1.append(row[6])
                            psfilepath1.append(row[13])
                        else:
                            psPostid.append("None")
                            pstitle1.append(private_title)
                            psdescription1.append(private_description)
                            psfilepath1.append(private_filepath)
            if has_posts:
                for pic in psfilepath1:
                    my_pic = Image.open(pic)
                    resized = my_pic.resize((320, 220))
                    new_pic = ImageTk.PhotoImage(resized)
                    images1.append(new_pic)

                title_label1 = Label(upFrame, text=pstitle1[post_num - 1], font=("Roboto", 13), padx=7,
                                     pady=5)
                image_label1 = Label(upFrame, image=images1[post_num - 1])
                description_label1 = Label(upFrame, text=psdescription1[post_num - 1],
                                           font=("Helvetica bold 18", 13), padx=7, pady=3)

                def forward(p_num):
                    global title_label1
                    global image_label1
                    global description_label1
                    global button_forward1
                    global button_back1
                    global button_comment
                    global images1

                    title_label1.grid_forget()
                    image_label1.grid_forget()
                    description_label1.grid_forget()

                    title_label1 = Label(upFrame, text=pstitle1[p_num - 1], font=("Roboto", 13), padx=7,
                                         pady=5)
                    image_label1 = Label(upFrame, image=images1[p_num - 1])
                    description_label1 = Label(upFrame, text=psdescription1[p_num - 1],
                                               font=("Helvetica bold 18", 13), padx=7, pady=3)

                    button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                             command=lambda: forward(p_num + 1))
                    button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                          command=lambda: back(p_num - 1))
                    if pstitle1[p_num-1] == "None":
                        button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                state="disabled")
                    else:
                        button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                command=lambda: Post.comment_on_a_post(psPostid[p_num-1], ID, self))

                    if p_num == len(images1):
                        button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13),
                                                 state="disabled")

                    title_label1.grid(row=0, column=0, sticky="W")
                    image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                    description_label1.grid(row=2, column=0, sticky="W", pady=7)
                    button_forward1.place(x=250, y=300)
                    button_comment.place(x=100, y=300)
                    button_back1.grid(row=3, column=0, sticky="W")

                def back(p_num):
                    global title_label1
                    global image_label1
                    global description_label1
                    global button_forward1
                    global button_back1
                    global button_comment
                    global images1

                    title_label1.grid_forget()
                    image_label1.grid_forget()
                    description_label1.grid_forget()

                    title_label1 = Label(upFrame, text=pstitle1[p_num - 1], font=("Roboto", 13), padx=7,
                                         pady=5)
                    image_label1 = Label(upFrame, image=images1[p_num - 1])
                    description_label1 = Label(upFrame, text=psdescription1[p_num - 1],
                                               font=("Helvetica bold 18", 13), padx=7, pady=3)

                    button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                             command=lambda: forward(p_num + 1))
                    button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                          command=lambda: back(p_num - 1))
                    if pstitle1[p_num-1] == "None":
                        button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                state="disabled")
                    else:
                        button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                command=lambda: Post.comment_on_a_post(psPostid[p_num-1], ID, self))

                    if p_num == 1:
                        button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13),
                                              state="disabled")

                    title_label1.grid(row=0, column=0, sticky="W")
                    image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                    description_label1.grid(row=2, column=0, sticky="W", pady=7)
                    button_forward1.place(x=250, y=300)
                    button_comment.place(x=100, y=300)
                    button_back1.grid(row=3, column=0, sticky="W")

                if len(images1) != 1:
                    button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                             command=lambda: forward(post_num + 1))
                    button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                          command=lambda: back(post_num))
                else:
                    button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                             state="disabled")
                    button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                          state="disabled")

                if pstitle1[post_num - 1] == "None":
                    button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                            state="disabled")
                else:
                    button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                            command=lambda: Post.comment_on_a_post(psPostid[post_num - 1], ID, self))

                title_label1.grid(row=0, column=0, sticky="W")
                image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                description_label1.grid(row=2, column=0, sticky="W", pady=7)
                button_forward1.place(x=250, y=300)
                button_comment.place(x=100, y=300)
                button_back1.grid(row=3, column=0, sticky="W")

            if not has_posts:
                Label(upFrame, text="User has no posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3,
                                                                                    sticky="W")
        else:
            # Else checking if you are friends with that user.
            friends = False
            with open("Friends.csv") as friend_file:
                csv_reader = csv.reader(friend_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID) and row[3] == str(ID) or row[0] == str(ID) and row[3] == str(self.ID):
                        friends = True
                        break
            if friends:
                post_num = 1

                has_posts = False
                with open("Posts.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(ID) and row[9] == str(0) and not row[12]:
                            psPostid.append(row[3])
                            pstitle1.append(row[5])
                            psdescription1.append(row[6])
                            psfilepath1.append(row[13])
                            has_posts = True
                        if row[0] == str(ID) and row[9] != str(0) and not row[12]:
                            has_posts = True
                            access_to_private_post = False
                            post_privacy_id = row[9]
                            # Checking if you've access to that private post.
                            with open("Privacy_lists.csv") as private_lst_file:
                                csv_reader = csv.reader(private_lst_file, delimiter=",")
                                for line in csv_reader:
                                    if line[0] == post_privacy_id and str(self.ID) in line[1]:
                                        access_to_private_post = True
                                        break
                            if access_to_private_post:
                                psPostid.append(row[3])
                                pstitle1.append(row[5])
                                psdescription1.append(row[6])
                                psfilepath1.append(row[13])
                            else:
                                psPostid.append("None")
                                pstitle1.append(private_title)
                                psdescription1.append(private_description)
                                psfilepath1.append(private_filepath)
                if has_posts:
                    for pic in psfilepath1:
                        my_pic = Image.open(pic)
                        resized = my_pic.resize((320, 220))
                        new_pic = ImageTk.PhotoImage(resized)
                        images1.append(new_pic)

                    title_label1 = Label(upFrame, text=pstitle1[post_num - 1], font=("Roboto", 13), padx=7,
                                         pady=5)
                    image_label1 = Label(upFrame, image=images1[post_num - 1])
                    description_label1 = Label(upFrame, text=psdescription1[post_num - 1],
                                               font=("Helvetica bold 18", 13), padx=7, pady=3)

                    def forward(p_num):
                        global title_label1
                        global image_label1
                        global description_label1
                        global button_forward1
                        global button_back1
                        global button_comment
                        global images1

                        title_label1.grid_forget()
                        image_label1.grid_forget()
                        description_label1.grid_forget()

                        title_label1 = Label(upFrame, text=pstitle1[p_num - 1], font=("Roboto", 13), padx=7,
                                             pady=5)
                        image_label1 = Label(upFrame, image=images1[p_num - 1])
                        description_label1 = Label(upFrame, text=psdescription1[p_num - 1],
                                                   font=("Helvetica bold 18", 13), padx=7, pady=3)

                        button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: forward(p_num + 1))
                        button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                              command=lambda: back(p_num - 1))
                        if pstitle1[p_num - 1] == "None":
                            button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13),
                                                    fg="#1877F2",
                                                    state="disabled")
                        else:
                            button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13),
                                                    fg="#1877F2",
                                                    command=lambda: Post.comment_on_a_post(psPostid[p_num - 1], ID,
                                                                                           self))

                        if p_num == len(images1):
                            button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13),
                                                     state="disabled")

                        title_label1.grid(row=0, column=0, sticky="W")
                        image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                        description_label1.grid(row=2, column=0, sticky="W", pady=7)
                        button_forward1.place(x=250, y=300)
                        button_comment.place(x=100, y=300)
                        button_back1.grid(row=3, column=0, sticky="W")

                    def back(p_num):
                        global title_label1
                        global image_label1
                        global description_label1
                        global button_forward1
                        global button_back1
                        global button_comment
                        global images1

                        title_label1.grid_forget()
                        image_label1.grid_forget()
                        description_label1.grid_forget()

                        title_label1 = Label(upFrame, text=pstitle1[p_num - 1], font=("Roboto", 13), padx=7,
                                             pady=5)
                        image_label1 = Label(upFrame, image=images1[p_num - 1])
                        description_label1 = Label(upFrame, text=psdescription1[p_num - 1],
                                                   font=("Helvetica bold 18", 13), padx=7, pady=3)

                        button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: forward(p_num + 1))
                        button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                              command=lambda: back(p_num - 1))
                        if pstitle1[p_num - 1] == "None":
                            button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13),
                                                    fg="#1877F2",
                                                    state="disabled")
                        else:
                            button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13),
                                                    fg="#1877F2",
                                                    command=lambda: Post.comment_on_a_post(psPostid[p_num - 1], ID,
                                                                                           self))

                        if p_num == 1:
                            button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13),
                                                  state="disabled")

                        title_label1.grid(row=0, column=0, sticky="W")
                        image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                        description_label1.grid(row=2, column=0, sticky="W", pady=7)
                        button_forward1.place(x=250, y=300)
                        button_comment.place(x=100, y=300)
                        button_back1.grid(row=3, column=0, sticky="W")

                    if len(images1) != 1:
                        button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: forward(post_num + 1))
                        button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                              command=lambda: back(post_num))
                    else:
                        button_forward1 = Button(upFrame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 state="disabled")
                        button_back1 = Button(upFrame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                              state="disabled")

                    if pstitle1[post_num - 1] == "None":
                        button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                state="disabled")
                    else:
                        button_comment = Button(upFrame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                command=lambda: Post.comment_on_a_post(psPostid[post_num - 1], ID,
                                                                                       self))

                    title_label1.grid(row=0, column=0, sticky="W")
                    image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                    description_label1.grid(row=2, column=0, sticky="W", pady=7)
                    button_forward1.place(x=250, y=300)
                    button_comment.place(x=100, y=300)
                    button_back1.grid(row=3, column=0, sticky="W")

                if not has_posts:
                    Label(upFrame, text="User has no posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3,
                                                                                        sticky="W")
            else:
                # You can't view user's post.
                Label(upFrame, text="You can't view posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3,
                                                                                       sticky="W")

    def accept_decline_friend_request(self):
        accept_decline = Toplevel()
        accept_decline.title("Friend Requests")
        accept_decline.iconbitmap(r"C:\Users\Saifia\Dropbox\My PC (DESKTOP-7HOSIO0)\Downloads\fbicon.ico")

        adFrame = LabelFrame(accept_decline, text="Friend Requests Pending", font=("Roboto", 15), fg="#1877F2", padx=50,
                             pady=30)
        adFrame.pack(padx=15, pady=15)

        Label(adFrame, text="New Friend Requests: ", font=("Roboto", 14), padx=5, pady=5, bd=1, relief="sunken",
              fg="#1877F2").grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        global request_to_accept
        global request_to_reject
        global friend_request
        global acl
        global adl
        global ta
        global la
        global ta_info
        global la_info

        l5 = Label(adFrame, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                   padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

        sender_first_name = []
        sender_last_name = []
        sender_id = []
        pending_friend_request = False
        with open("Friends.csv") as friend_file:
            csv_reader = csv.reader(friend_file, delimiter=",")
            for row in csv_reader:
                if row[3] == str(self.ID) and row[6] == str(True):
                    pending_friend_request = True
                    sender_first_name.append(row[1])
                    sender_last_name.append(row[2])
                    sender_id.append(row[0])
                    break

        def accept_request(friend_request_no, sen_ID, row_no):
            global request_to_accept
            global acl
            global request_to_reject
            global adl

            r = csv.reader(open("Friends.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][3] == str(self.ID) and lines[lst][6] == str(True) and lines[lst][0] == \
                        sen_ID[int(friend_request_no)-1]:
                    lines[lst][4], lines[lst][5], lines[lst][6] = self.first_name, self.last_name, False
            writer = csv.writer(open("Friends.csv", "w", newline=""))
            writer.writerows(lines)

            request_to_accept.grid_forget()
            acl.grid_forget()

            request_to_accept.grid_forget()
            acl.grid_forget()
            request_to_reject.grid_forget()
            adl.grid_forget()

            take_action(row_no)

        def decline_request(friend_request_no, sen_ID, row_no):
            global request_to_accept
            global acl
            global request_to_reject
            global adl

            r = csv.reader(open("Friends.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][3] == str(self.ID) and lines[lst][6] == str(True) and lines[lst][0] == \
                        sen_ID[int(friend_request_no) - 1]:
                    lines.remove(lines[lst])
                    break
            writer = csv.writer(open("Friends.csv", "w", newline=""))
            writer.writerows(lines)

            request_to_accept.grid_forget()
            acl.grid_forget()
            request_to_reject.grid_forget()
            adl.grid_forget()

            take_action(row_no)

        def take_action(row_no):
            global ta
            global la
            global acl
            global adl
            global request_to_accept
            global request_to_reject
            global ta_info
            global la_info
            if ta.grid_info() != {}:
                ta.grid_forget()
            if la.grid_info() != {}:
                la.grid_forget()
            acl = Label(adFrame, text="Number of request\nyou want to accept: ", font=("Roboto", 13), padx=4, pady=5,
                        bd=1, relief="sunken")
            acl.grid(row=row_no + 1, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            request_to_accept = Entry(adFrame, highlightthickness=2)
            request_to_accept.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            request_to_accept.grid(row=row_no + 1, column=2, sticky="E")

            adl = Label(adFrame, text="Number of request\nyou want to decline: ", font=("Roboto", 13), padx=4, pady=5,
                        bd=1, relief="sunken")
            adl.grid(row=row_no + 3, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            request_to_reject = Entry(adFrame, highlightthickness=2)
            request_to_reject.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            request_to_reject.grid(row=row_no + 3, column=2, sticky="E")

            acb = Button(adFrame, text="Accept", font=("Roboto", 13), width=7, bg="#1877F2", fg="white",
                         command=lambda: accept_request(request_to_accept.get(), sender_id, row_no))
            acb.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")

            deb = Button(adFrame, text="Decline", font=("Roboto", 13), width=10, bg="#1877F2", fg="white",
                         command=lambda: decline_request(request_to_reject.get(), sender_id, row_no))
            deb.grid(row=row_no+4, column=0, columnspan=3, pady=7, sticky="W")

            Button(adFrame, text="Done", font=("Roboto", 13), width=10, command=lambda: accept_decline.destroy())\
                .grid(row=row_no + 5, column=0, columnspan=3, pady=7, sticky="W")

        if pending_friend_request:

            row_no = 1

            with open("Friends.csv") as friend_file:
                csv_reader = csv.reader(friend_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == str(self.ID) and row[6] == str(True):
                        Label(adFrame, text=f"You've a new friend request\nfrom {row[1]} {row[2]}.",
                              font=("Roboto", 13), padx=20, pady=5, bd=1, relief="groove").grid(row=row_no, column=0,
                                                                                                columnspan=2, pady=10,
                                                                                                padx=3, sticky="W")
                        row_no += 1

            ta = Button(adFrame, text="Take Action", font=("Roboto", 13), width=12, bg="#1877F2", fg="white",
                        command=lambda: take_action(row_no))
            ta.grid(row=row_no+1, column=0, columnspan=3, pady=7, sticky="W")
            ta_info = ta.grid_info()
            la = Button(adFrame, text="Later", font=("Roboto", 13), width=10, bg="#1877F2", fg="white",
                        command=lambda: accept_decline.destroy())
            la.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")
            la_info = la.grid_info()

        else:
            Label(adFrame, text="No new friend requests.", font=("Roboto", 13), padx=20, pady=4, bd=1, relief="groove").\
                grid(row=0, column=0, padx=4, pady=7, sticky="W")


u1 = User()


def GUI(obj):
    # Initial Frame.
    global myFrame
    myFrame = LabelFrame(root, padx=70, pady=70, text="Welcome to Facebook", font=("Roboto", 18), fg="#1877F2")
    myFrame.pack(padx=50, pady=25)

    # Login and Sign Up Buttons.
    global loginButton
    loginButton = Button(myFrame, text="Login", padx=35, pady=10, font=("Roboto", 14), command=obj.login)
    Label(myFrame, text="OR", font="Roboto", fg="#1877F2").grid(row=1, column=1, pady=10)
    global signButton
    signButton = Button(myFrame, text="Sign Up", padx=35, pady=10, font=("Roboto", 14),
                        command=obj.sign_up)

    loginButton.grid(row=0, column=1)
    signButton.grid(row=2, column=1)

    root.mainloop()


GUI(u1)
