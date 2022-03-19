from typing import Dict, Optional

from ctfd.awards import AwardsClient
from ctfd.challenges import ChallengesClient
from ctfd.comments import CommentsClient
from ctfd.configs import ConfigsClient
from ctfd.files import FilesClient
from ctfd.flags import FlagsClient
from ctfd.hints import HintsClient
from ctfd.notifications import NotificationsClient
from ctfd.pages import PagesClient
from ctfd.scoreboard import ScoreboardClient
from ctfd.statistics import StatisticsClient
from ctfd.submissions import SubmissionsClient
from ctfd.tags import TagsClient
from ctfd.teams import TeamsClient
from ctfd.tokens import TokensClient
from ctfd.topics import TopicsClient
from ctfd.unlocks import UnlocksClient
from ctfd.users import UsersClient

from . import utils
from .api_result import APIResult


class CTFd:
    def get(self, uri: str, /, *, params: Optional[Dict[str, str]] = None) -> APIResult:
        url = f"{self._host}/api/v1{uri}"

        response = self._session.get(url, params=params)
        data = response.json()

        return APIResult.parse_obj(data)

    def __init__(self, host: str, token: str, /, *, verify_tls: bool = True) -> None:
        self._host = host
        self._session = utils.create_session(verify_tls=verify_tls, token=token)

        self.awards = AwardsClient(self)
        self.challenges = ChallengesClient(self)
        self.comments = CommentsClient(self)
        self.configs = ConfigsClient(self)
        self.files = FilesClient(self)
        self.flags = FlagsClient(self)
        self.hints = HintsClient(self)
        self.notifications = NotificationsClient(self)
        self.pages = PagesClient(self)
        self.scoreboard = ScoreboardClient(self)
        self.statistics = StatisticsClient(self)
        self.submissions = SubmissionsClient(self)
        self.tags = TagsClient(self)
        self.teams = TeamsClient(self)
        self.tokens = TokensClient(self)
        self.topics = TopicsClient(self)
        self.unlocks = UnlocksClient(self)
        self.users = UsersClient(self)
