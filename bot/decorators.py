import discord.ext.commands as disextc
import logging as lg
import typing as typ

import constants

# Log instance for this module
log = lg.getLogger(__name__)


# Checks

async def author_is_developer(ctx: disextc.Context) -> bool:
    """ Check to see if author id is the developer. """
    return ctx.author.id == constants.id_bloodythorn


async def author_is_wiihacky(ctx: disextc.Context) -> bool:
    """ Check to see if the message came from the official bot. """
    # TODO: Second thought tells me a decorator won't be useful for this check
    #   as most bot messages are ignored, and no commands will come from the
    #   bot.
    return ctx.guild.id == constants.id_wiihacky


async def was_sent_from_wiihacks(ctx: disextc.Context) -> bool:
    """ Check to see if the message came from the official discord. """
    return ctx.guild.id == constants.id_wiihacks


# Decorators

def has_role(role_names) -> typ.Callable:
    """ This will check to see if the user has one of the roles provided. """
    async def predicate(ctx: disextc.Context) -> bool:
        if not ctx.guild:  # Return False in a DM
            log.debug(
                f"{ctx.author} tried to use the '{ctx.command.name}'" 
                "command from a DM. "
                "This command is restricted by the with_role decorator."
                "Rejecting request.")
            raise disextc.CommandError("Cannot run command from DM.")
        exe_roles = [a.name for a in ctx.message.author.roles]
        for role in role_names:
            if role in exe_roles:
                return True
        raise disextc.CommandError(f'You do not have permissions to use this.')
    return disextc.check(predicate)


def is_developer() -> typ.Callable:
    """Decorator for author_is_developer."""
    return disextc.check(author_is_developer)


def is_wiihacks() -> typ.Callable:
    """Decorator for was_sent_from_wiihacks."""
    return disextc.check(was_sent_from_wiihacks)


def log_invocation() -> typ.Callable:
    """ Log Invocation Context.

    This decorator will make sure the invocation context of the command is
        logged.
    """
    async def predicate(ctx: disextc.Context) -> bool:
        txt_log_out = 'Log Invocation Context: {}'
        log.info(txt_log_out.format(vars(ctx)))
        system = ctx.bot.get_cog('System')
        if system is not None:
            await system.send_to_log(
                f'User: {ctx.author.name}#{ctx.author.discriminator} ' +
                f'has invoked the {ctx.invoked_with} command')
        return True
    return disextc.check(predicate)