from playwright.sync_api import Page, expect
import os

# // Keybord comands
def keyBoardEvents(page: Page):
    page.goto("https://www.amazon.in/")
    page.locator("input#twotabsearchtextbox").fill("iphone")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)
    # page.keyboard.press("Escape")
    # Press and Release Keys Separately
    # page.keyboard.down("Control")
    # # page.keyboard.press("KeyA")
    # page.keyboard.up("Control")

    # # Keyboard Shortcuts (Combination Keys)
    page.keyboard.press("Control+A")   # Select all
    # page.keyboard.press("Control+C")   # Copy
    # page.keyboard.press("Control+V")   # Paste





def mouseEvents(page:Page):
    # page.goto("https://www.amazon.in/")
    # page.hover("//span[contains(text(),'Account & Lists')]")
    # page.mouse.move(300, 200)
    # page.mouse.down()
    # page.mouse.up()
    # Drag and Drop (Using Mouse)
    page.goto("https://practice.expandtesting.com/drag-and-drop?utm_source=chatgpt.com")
    # source = page.locator(page.locator("#column-a"))
    # target = page.locator("#column-b")
    # source = "#column-a"
    # target ="#column-b"
    # page.drag_and_drop(source,target)
    # # Scroll Using Mouse Wheel
    # page.locator("#column-b").scroll_into_view_if_needed()
    # page.mouse.wheel(0,400)   # Vertical scroll
    # page.mouse.wheel(500, 0)   # Horizontal scroll
    # # # Right Click
    # page.locator("#column-a").click(button="right")
    # page.click("#element", button="right")
    # # Double Click
    # page.dblclick("#element")

    # page.click("#column-a", button="right")
    # page.click("#column-b")

    # page.locator("#column-a").fill("Dragged")
    # page.fill("#column-b","Dragged")



# lambda dialog: dialog.click("text=hello")

def alerts(page:Page):
    
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    def handleAlert(dialog):
        dialog.dismiss("text=Hello")
    page.once("dialog", handleAlert)
    page.locator("//button[@onclick='jsPrompt()']").click()

    

# def alerts(page:Page):
#     page.goto("https://the-internet.herokuapp.com/javascript_alerts")
#     # simpleAlert  
#     page.once("dialog", lambda dialog: dialog.accept())
#     def handle_dialog(dialog):
#         print("Alert text is:", dialog.message)
#         dialog.accept()
#     page.once("dialog", handle_dialog)
#     page.click("text=Click for JS Alert")
#     # page.once("dialog", lambda dialog: dialog.accept())
#     # page.click("text=Click for JS Alert")
#     # # Confirm Alert (OK / Cancel)
#     # page.once("dialog", lambda dialog: dialog.accept())
#     # page.click("text=Click for JS Confirm")
#     # page.once("dialog", lambda dialog: dialog.dismiss())
#     # page.click("text=Click for JS Confirm")
#     # #Promt based alert
#     # page.once("dialog",lambda dialog: dialog.accept("Playwright Alert"))
#     # page.click("text=Click for JS Prompt")


def fileUpload(page:Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    # page.hover("text=File Uploader")
    page.set_input_files("#file-upload", "testData\\credentails.csv")
    # page.set_input_files("#file-upload", "testData\\credentails.csv")
    page.click("#file-submit")

def test_file_download(page: Page):
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.click("text=some-file.txt")
    download = download_info.value
    print(download)
    file_path = "download/" + download.suggested_filename
    download.save_as(file_path)
    assert os.path.exists(file_path)


def datePickers(page:Page):
    page.goto("https://jqueryui.com/datepicker/")
    # page.frame_locator(".demo-frame").locator("input#datepicker").fill("02/01/2026")
    frame = page.frame_locator(".demo-frame")
    # frame.locator("input#datepicker").fill("02/01/2026")
    frame.locator("input#datepicker").click()
    month = frame.locator(".ui-datepicker-month").text_content()
    print(month)
    if(month=='January'):
        frame.locator("//a[@data-date='11']").click()


# def test_navigate_to_january(page: Page):
#     page.goto("https://jqueryui.com/datepicker/")

#     frame = page.frame_locator(".demo-frame")
#     frame.locator("#datepicker").click()

#     target_month = "April"
#     months = [
#         "January", "February", "March", "April", "May", "June",
#         "July", "August", "September", "October", "November", "December"
#     ]

#     while True:
#         current_month = frame.locator(".ui-datepicker-month").text_content()

#         if current_month == target_month:
#             frame.locator("//a[text()='11']").click()
#             break

#         # Compare index to decide direction
#         if months.index(current_month) > months.index(target_month):
#             frame.locator(".ui-datepicker-prev").click()
#         else:
#             frame.locator(".ui-datepicker-next").click()











