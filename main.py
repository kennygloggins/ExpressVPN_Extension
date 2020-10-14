import json
import logging
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


def create_item(name, image, keyword, description, on_enter):
    return (
        keyword,
        ExtensionResultItem(
            name=name,
            description=description,
            icon=image,
            on_enter=RunScriptAction(on_enter, None),
        ),
    )


class ExpressVPN_Extension(Extension):
    def __init__(self):
        super(ExpressVPN_Extension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


items_cache = [
    create_item("Connect", "images/connect.png", "connect", "Connect to VPN", "expressvpn connect"),
    create_item(
        "Disconnect", "images/disconnect.png", "disconnect", "Disconnect from VPN", "expressvpn disconnect"
    ),
]


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        term = (event.get_argument() or "").lower()
        items = [i for name, i in items_cache if name.startswith(term)]
        return RenderResultListAction(items)


if __name__ == "__main__":
    ExpressVPN_Extension().run()
