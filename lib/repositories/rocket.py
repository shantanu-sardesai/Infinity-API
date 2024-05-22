from typing import Union
from lib import logging, parse_error
from lib.models.rocket import Rocket
from lib.repositories.repo import Repository

logger = logging.getLogger(__name__)


class RocketRepository(Repository):
    """
    Enables database CRUD operations with models.Rocket

    Init Attributes:
        rocket: models.Rocket
        rocket_id: str

    """

    def __init__(self):
        super().__init__("rockets")

    @classmethod
    def fetch_rocket(cls, rocket: Rocket):
        instance = cls()
        instance.rocket = rocket
        instance.rocket_id = rocket.rocket_id
        return instance

    @property
    def rocket(self) -> Rocket:
        return self._rocket

    @rocket.setter
    def rocket(self, rocket: "Rocket"):
        self._rocket = rocket

    @property
    def rocket_id(self) -> str:
        return self._rocket_id

    @rocket_id.setter
    def rocket_id(self, rocket_id: "str"):
        self._rocket_id = rocket_id

    async def create_rocket(
        self, *, rocket_option: str = "CALISTO", motor_kind: str = "SOLID"
    ):
        """
        Creates a non-existing models.Rocket in the database

        Args:
            rocket_option: models.rocket.RocketOptions
            motor_kind: models.motor.MotorKinds

        Returns:
            self
        """
        try:
            rocket_to_dict = self.rocket.dict()
            rocket_to_dict["rocket_id"] = self.rocket_id
            rocket_to_dict["rocket_option"] = rocket_option
            rocket_to_dict["motor"]["motor_kind"] = motor_kind
            await self.collection.insert_one(rocket_to_dict)
        except Exception as e:
            exc_str = parse_error(e)
            logger.error(f"repositories.rocket.create_rocket: {exc_str}")
            raise Exception(f"Error creating rocket: {exc_str}") from e
        else:
            return self
        finally:
            logger.info(
                f"Call to repositories.rocket.create_rocket completed for Rocket {self.rocket_id}"
            )

    async def get_rocket_by_id(self, rocket_id: str) -> Union[Rocket, None]:
        """
        Gets a models.Rocket from the database

        Returns:
            models.Rocket
        """
        try:
            read_rocket = await self.collection.find_one(
                {"rocket_id": rocket_id}
            )
            parsed_rocket = (
                Rocket.parse_obj(read_rocket) if read_rocket else None
            )
        except Exception as e:
            exc_str = parse_error(e)
            logger.error(f"repositories.rocket.get_rocket: {exc_str}")
            raise Exception(f"Error getting rocket: {exc_str}") from e
        else:
            return parsed_rocket
        finally:
            logger.info(
                f"Call to repositories.rocket.get_rocket completed for Rocket {rocket_id}"
            )

    async def delete_rocket_by_id(self, rocket_id: str):
        """
        Deletes a models.Rocket from the database

        Returns:
            None
        """
        try:
            await self.collection.delete_one({"rocket_id": rocket_id})
        except Exception as e:
            exc_str = parse_error(e)
            logger.error(f"repositories.rocket.delete_rocket: {exc_str}")
            raise Exception(f"Error deleting rocket: {exc_str}") from e
        finally:
            logger.info(
                f"Call to repositories.rocket.delete_rocket completed for Rocket {rocket_id}"
            )
