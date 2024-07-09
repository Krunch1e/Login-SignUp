import customtkinter as ctk

ctk.set_default_color_theme("PythonDjangoBanaoTask/Themes/Hacked/hacked.json")

main_window = ctk.CTk()
main_window.title('Banao Task- 1')
main_window.geometry('550x600')
main_window.resizable(False, False)

main_label = ctk.CTkLabel(
    main_window,
    text = 'Login/Signup Window',
    corner_radius = 15,
    font = ('Ariel',15)
)
main_label.pack()

login_button = ctk.CTkButton(
    main_window,
    text = 'Login',
    font = ('Ariel',15),
    hover_color = '#770',
    # command = lambda: 
    )
login_button.pack()

main_window.mainloop()