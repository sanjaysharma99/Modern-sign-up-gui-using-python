import customtkinter as ctk

app=ctk.CTk()
ctk.set_appearance_mode('dark')

sign_up_frame=ctk.CTkFrame(app)
sign_up_frame.pack(expand=True,padx=50,pady=50)

sign_up_label=ctk.CTkLabel(sign_up_frame,
                           text='Sign Up',
                           text_color='white',
                           font=('Robot',18))
sign_up_label.pack(pady=5)

email=ctk.CTkEntry(sign_up_frame,
                   width=250,
                   height=35,
                   placeholder_text='Enter your email')
email.pack(pady=8,padx=25)

password=ctk.CTkEntry(sign_up_frame,
                      width=250,
                      height=35,
                      show='*',
                      placeholder_text='Create a password')
password.pack(pady=8,padx=25)

confirm_password=ctk.CTkEntry(sign_up_frame,
                              width=250,
                              height=35,
                              show='*',
                              placeholder_text='Confirm your password')
confirm_password.pack(pady=8,padx=25)

sign_up_btn=ctk.CTkButton(sign_up_frame,
                          text='Sign Up',
                          width=250,
                          height=35)
sign_up_btn.pack(padx=8,pady=25)

aready_account_frame=ctk.CTkFrame(sign_up_frame,
                                  fg_color='transparent')
aready_account_frame.pack(pady=5)

aready_account_label=ctk.CTkLabel(aready_account_frame,
                                  text='Already have an account?',
                                  font=('Roboto',12))
aready_account_label.pack(side='left',padx=4)

login_url=ctk.CTkLabel(aready_account_frame,
                       text='Login',
                       font=('Roboto',12))
login_url.pack(side='left')

app.mainloop()
