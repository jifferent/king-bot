from .utils import log
from .util_game import close_modal
from .custom_driver import client
from enum import Enum

# todo check if already in village/city or ress


class building(Enum):
    smithy = 13
    headquarter = 15
    rallypoint = 16
    market = 17
    barracks = 19
    academy = 22
    residence = 25


def open_village(browser: client, id: int) -> None:
    index = id

    btn = browser.find("//a[@id='villageOverview']")
    browser.click(btn, 1)
    table = browser.find(
        "//table[contains(@class, 'villagesTable')]/tbody")
    villages = table.find_elements_by_xpath(".//tr")

    tds = villages[index].find_elements_by_xpath(".//td")
    link = tds[0].find_element_by_xpath(".//a")
    browser.click(link, 1)

    log("opened village {}".format(index))
    close_modal(browser)


def open_city(browser: client) -> None:
    btn = browser.find("//a[@id='optimizly_mainnav_village']")
    browser.click(btn, 1)


def open_resources(browser: client) -> None:
    btn = browser.find("//a[@id='optimizly_mainnav_resources']")
    browser.click(btn, 1)


def open_building(browser: client, building: int) -> None:
    # todo open by slot id
    img = browser.find(
        "//img[@id='buildingImage{}']".format(building))
    browser.click(img, 1)


def open_building_type(browser: client, b_type: building) -> None:
    view = browser.find("//div[@id='villageView']")
    locations = view.find_elements_by_xpath(".//building-location")

    for loc in locations:
        classes = loc.get_attribute("class")

        if "free" not in classes:
            img = loc.find_element_by_xpath(".//img")
            classes = img.get_attribute("class")
            class_list = classes.split(" ")

            for c in class_list:
                if c == "buildingId{}".format(b_type.value):
                    browser.click(img)
                    return
