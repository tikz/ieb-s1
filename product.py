import json
import logging
import os

from cryptography.fernet import Fernet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Product:
    def __init__(self):
        self.pending = True
        self.error = None

    def from_json(self, raw: bytes):
        j = json.loads(raw)

        try:
            self.id = j["id"]
            self.code = j["code"]
            self.cost = j["cost"]
            self.price = j["price"]
            self.description = j["description"]
        except Exception as e:
            self.error = j["detail"] if "detail" in j else repr(e)
        else:
            self.error = None
        finally:
            self.pending = False

    def unserialize(self, raw: bytes):
        self.from_json(raw)
        return self

    def serialize(self) -> bytes:
        return bytes(json.dumps(self.__dict__), encoding="utf-8")

    def pretty_print(self):
        logging.info(f"Producto {self.code}")
        logging.info(f"\t$ {self.cost}")
        logging.info(f"\t$ {self.price}")
        logging.info(f"\t {self.description}")


class ProductEncrypted(Product):
    fernet = Fernet(os.getenv("ENCRYPTION_KEY"))

    def unserialize(self, raw: bytes):
        raw = self.fernet.decrypt(raw)
        super().from_json(raw)
        return self

    def serialize(self) -> bytes:
        return self.fernet.encrypt(super().serialize())
