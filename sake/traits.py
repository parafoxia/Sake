"""Traits for the cache resources defined by this standard."""

from __future__ import annotations

__all__: typing.Final[typing.Sequence[str]] = [
    "Resource",
    "EmojiCache",
    "GuildCache",
    "GuildChannelCache",
    "InviteCache",
    "MeCache",
    "MemberCache",
    "PresenceCache",
    "RoleCache",
    "UserCache",
    "VoiceStateCache",
]

import typing

if typing.TYPE_CHECKING:
    from hikari import channels
    from hikari import emojis
    from hikari import guilds
    from hikari import invites
    from hikari import presences
    from hikari import snowflakes
    from hikari import traits as _traits
    from hikari import users
    from hikari import voices

    from sake import views


class Resource(typing.Protocol):
    """The basic interface which all cache resources should implement."""

    __slots__: typing.Sequence[str] = ()

    def subscribe_listeners(self) -> None:
        """Register this resource's internal listener to a dispatcher aware app.

        !!! note
            Dependent on the implementation, this may be called by
            `Resource.open` and may raise a `builtins.TypeError`if called
            when this resource's listeners have already been registered.

        !!! note
            If the event dispatcher isn't provided during initialisation then
            this method will do nothing.
        """
        raise NotImplementedError

    def unsubscribe_listeners(self) -> None:
        """Unregister this resource's internal listener to a dispatcher aware app.

        !!! note
            Dependent on the implementation, this may be called by
            `Resource.close` and may raise a `builtins.TypeError`if called
            when this resource's listeners haven't been registered yet.

        !!! note
            If the event dispatcher isn't provided during initialisation then
            this method will do nothing.
        """
        raise NotImplementedError

    async def open(self) -> None:
        """Startup the resource(s) and allow them to connect to their relevant backend(s).

        !!! note
            This should implicitly call `Resource.subscribe_listeners`.

        !!! note
            This should pass without raising if called on an already opened
            resource.
        """
        raise NotImplementedError  # TODO: connection errors.

    async def close(self) -> None:
        """Close the resource(s) and allow them to disconnect from their relevant backend(s).

        !!! note
            This should implicitly call `Resource.unsubscribe_listeners`.

        !!! note
            This should pass without raising if called on an already closed
            resource.
        """
        raise NotImplementedError


class EmojiCache(Resource, typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def clear_emojis(self) -> None:
        raise NotImplementedError

    async def clear_emojis_for_guild(self, guild_id: snowflakes.Snowflakeish) -> None:
        raise NotImplementedError

    async def delete_emoji(self, emoji_id: snowflakes.Snowflakeish) -> None:
        raise NotImplementedError

    async def get_emoji(self, emoji_id: snowflakes.Snowflakeish) -> emojis.KnownCustomEmoji:
        raise NotImplementedError

    async def get_emoji_view(self) -> views.CacheView[snowflakes.Snowflake, emojis.KnownCustomEmoji]:
        raise NotImplementedError

    async def get_emoji_view_for_guild(
        self, guild_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, emojis.KnownCustomEmoji]:
        raise NotImplementedError

    async def set_emoji(self, emoji: emojis.KnownCustomEmoji) -> None:
        raise NotImplementedError


class GuildCache(Resource, typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def delete_guild(self, guild_id: snowflakes.Snowflakeish) -> None:
        raise NotImplementedError

    async def get_guild(self, guild_id: snowflakes.Snowflakeish) -> guilds.GatewayGuild:
        raise NotImplementedError

    async def get_guild_view(self) -> views.CacheView[snowflakes.Snowflake, guilds.GatewayGuild]:
        raise NotImplementedError

    async def set_guild(self, guild: guilds.GatewayGuild) -> None:
        raise NotImplementedError


class GuildChannelCache(Resource, typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def delete_guild_channel(self, channel_id: snowflakes.Snowflakeish) -> None:
        raise NotImplementedError

    async def get_guild_channel(self, channel_id: snowflakes.Snowflakeish) -> channels.GuildChannel:
        raise NotImplementedError

    async def get_guild_channel_view_for_guild(
        self, guild_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, channels.GuildChannel]:
        raise NotImplementedError

    async def set_guild_channel(self, channel: channels.GuildChannel) -> None:
        raise NotImplementedError


class InviteCache(Resource, typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def delete_invite(self, invite_code: str) -> None:
        raise NotImplementedError

    async def get_invite(self, invite_code: str) -> invites.InviteWithMetadata:
        raise NotImplementedError

    async def get_invites_view(self) -> views.CacheView[str, invites.InviteWithMetadata]:
        raise NotImplementedError

    async def get_invite_view_for_channel(
        self, channel_id: snowflakes.Snowflakeish
    ) -> views.CacheView[str, invites.InviteWithMetadata]:
        raise NotImplementedError

    async def get_invite_view_for_guild(
        self, guild_id: snowflakes.Snowflakeish
    ) -> views.CacheView[str, invites.InviteWithMetadata]:
        raise NotImplementedError

    async def set_invite(self, invite: invites.InviteWithMetadata) -> None:
        raise NotImplementedError


class MeCache(Resource, typing.Protocol):  # TODO: is this necessary?
    __slots__: typing.Sequence[str] = ()

    async def delete_me(self) -> None:
        raise NotImplementedError

    async def get_me(self) -> users.OwnUser:
        raise NotImplementedError

    async def set_me(self) -> None:
        raise NotImplementedError


class MemberCache(Resource, typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def delete_member(self, user_id: snowflakes.Snowflakeish) -> None:
        raise NotImplementedError

    async def get_member(self, guild_id: snowflakes.Snowflakeish, user_id: snowflakes.Snowflakeish) -> guilds.Member:
        raise NotImplementedError

    async def get_member_view_for_guild(
        self, guild_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, guilds.Member]:
        raise NotImplementedError

    async def get_member_view_for_user(
        self, user_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, guilds.Member]:
        raise NotImplementedError

    async def get_member_view(
        self,
    ) -> views.CacheView[snowflakes.Snowflakeish, views.CacheView[snowflakes.Snowflake, guilds.Member]]:
        raise NotImplementedError

    async def set_member(self, member: guilds.Member) -> None:
        raise NotImplementedError


class PresenceCache(Resource, typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def delete_presence(self, guild_id: snowflakes.Snowflakeish, user_id: snowflakes.Snowflakeish) -> None:
        raise NotImplementedError

    async def get_presence(
        self, guild_id: snowflakes.Snowflakeish, user_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, presences.MemberPresence]:
        raise NotImplementedError

    async def get_presence_view(
        self,
    ) -> views.CacheView[snowflakes.Snowflake, views.CacheView[snowflakes.Snowflake, presences.MemberPresence]]:
        raise NotImplementedError

    async def get_presence_view_for_user(
        self, user_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, presences.MemberPresence]:
        raise NotImplementedError

    async def get_presence_view_for_guild(
        self, guild_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, presences.MemberPresence]:
        raise NotImplementedError

    async def set_presence(self, presence: presences.MemberPresence) -> None:
        raise NotImplementedError


class RoleCache(Resource, typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def delete_role(self, role_id: snowflakes.Snowflakeish) -> None:
        raise NotImplementedError

    async def get_role(self, role_id: snowflakes.Snowflakeish) -> guilds.Role:
        raise NotImplementedError

    async def get_role_view(self) -> views.CacheView[snowflakes.Snowflake, guilds.Role]:
        raise NotImplementedError

    async def get_role_view_for_guild(
        self, guild_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, guilds.Role]:
        raise NotImplementedError

    async def set_role(self, role: guilds.Role) -> None:
        raise NotImplementedError


class UserCache(Resource, typing.Protocol):  # TODO: add this to more classes?
    """The traits for a cache implementation which supports a user cache.

    !!! note
        Unlike other resources, user is read only and will only ever be
        implemented as a part of another resource which references user objects
        due to the fact that it doesn't match up to any specific events.
    """

    __slots__: typing.Sequence[str] = ()

    # async def delete_user(self) -> None:
    #     raise NotImplementedError

    async def get_user(self, user_id: snowflakes.Snowflakeish) -> users.User:
        raise NotImplementedError

    async def get_user_view(self) -> views.CacheView[snowflakes.Snowflake, users.User]:
        raise NotImplementedError

    # async def set_user(self, user: users.User) -> None:
    #     raise NotImplementedError


class VoiceStateCache(Resource, typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def delete_voice_state(self, guild_id: snowflakes.Snowflakeish, user_id: snowflakes.Snowflakeish) -> None:
        raise NotImplementedError

    async def get_voice_state(
        self, guild_id: snowflakes.Snowflakeish, user_id: snowflakes.Snowflakeish
    ) -> voices.VoiceState:
        raise NotImplementedError

    async def get_voice_state_view_for_channel(
        self, channel_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, voices.VoiceState]:
        raise NotImplementedError

    async def get_voice_state_view_for_guild(
        self, guild_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, voices.VoiceState]:
        raise NotImplementedError

    async def get_voice_state_view_for_user(
        self, user_id: snowflakes.Snowflakeish
    ) -> views.CacheView[snowflakes.Snowflake, views.CacheView[snowflakes.Snowflake, voices.VoiceState]]:
        raise NotImplementedError

    async def set_voice_state(self, voice_state: voices.VoiceState) -> None:
        raise NotImplementedError
