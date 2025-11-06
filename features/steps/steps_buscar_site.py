from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import time
from behave import given, when, then

@given('Que o navegador esteja na página inicial')
def step_open_browser(context):

    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=options
    )

    context.driver.get("https://www.google.com")
    time.sleep(3)