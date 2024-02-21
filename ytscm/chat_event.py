"""
YouTube Super Chat Monitor
Copyright (C) 2020 Remington Creative

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from ytscm.author import YTChatAuthorDetails


class YTChatEvent:
    """
    Contains YouTube Chat event attributes.
    """

    """
    The ID that YouTube assigns to uniquely identify the Chat event.
    """
    __id = None

    """
    The YouTube channel ID that identifies the channel that autors the
    message
    """
    __author_channel_id = None

    """
    Details about the supporter's channel.
    """
    __supporter_details = None

    """
    The text content of the supporter's comment.
    """
    __comment_text = None

    """
    The date and time when the Super Chat was purchased. The value is specified 
    in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.
    """
    __created_at = None

    def __init__(self, chat_json):
        """
        Creates an object from a JSON super chat event object
        :param chat_json: the JSON super chat event        
        """

        self.__id = chat_json['id']
        self.__author_details = YTChatAuthorDetails(
            chat_json['authorDetails']
        )
        self.__comment_text = chat_json['snippet']['displayMessage']
        self.__created_at = chat_json['snippet']['publishedAt']
        

    def get_id(self):
        return self.__id

    def get_author_details(self):
        return self.__author_details

    def get_comment_text(self):
        return self.__comment_text

    def get_created_at(self):
        return self.__created_at    

    def __eq__(self, other):
        return self.__id == other.__id
