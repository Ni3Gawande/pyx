def add_before_ui_after_ui(func): #or use test_ui
    def wrapper():
        print("Before running UI TC")
        print("Start the browser")
        func() #or tes_ui()
        print("Ending the running UI TC")
        print("Quit the browser")
    return wrapper()


@add_before_ui_after_ui
def tes_ui():
    print("I will test the ui")