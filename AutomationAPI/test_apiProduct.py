from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

from utils.readingJson import readJsonData

# def test_getApi(playwright: sync_playwright):
#     # browser = playwright.chromium.launch()
#     # context = browser.new_context()
#     # page = context.new_page()
#     # auth = {
#     #     "user": "admin",
#     #     "password": "password123"
#     # }
#     # token = getDatafromJSON()
#     context = playwright.request.new_context()
#     response =  context.get("https://dummyjson.com/products/1", headers={"Authorization": "Bearer 343646464", "accept": "application/json"})
#     # print(response.status)
#     # print(response.status_text)
#     data = response.json()
#     print(data["description"])
#     # print(response.body())
#     assert response.status == 200
#     # assert data["title"] == "Essence Mascara Lash"


# def test_postApi(playwright: sync_playwright):
#     context = playwright.request.new_context()
#     insertionData = readJsonData("C:\\Users\\Nikitha\\Desktop\\training_26Nov_Batch\\testAutomationPOMFrameWork\\testData\\api.json")

#     response =  context.post("https://dummyjson.com/products/1", headers={"Authorization": "Bearer 343646464","Content-Type": "application/json"}, data=insertionData)

#     print(response.json())
#     assert response.status == 200


# def test_getapi(playwright: sync_playwright):
#     context = playwright.request.new_context()

#     response = context.get("https://gorest.co.in/public/v2/users", params={"id": 8115090})
#     print(response.json())
    
