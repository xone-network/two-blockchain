from typing import Optional

import click


@click.group("staking", short_help="Manage your staking")
@click.pass_context
def staking_cmd(ctx: click.Context) -> None:
    pass


@staking_cmd.command("info", short_help="Query staking info")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
def staking_info(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
) -> None:
    import asyncio
    from .wallet_funcs import execute_with_wallet, staking_info

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, {}, staking_info))


@staking_cmd.command("send", short_help="Send two to staking address")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option("-a", "--amount", help="How much two to send, in XTWO", type=str, required=True)
def staking_send_cmd(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
    amount: str,
) -> None:
    extra_params = {
        "amount": amount,
    }
    import asyncio
    from .wallet_funcs import execute_with_wallet, staking_send

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, staking_send))


@staking_cmd.command("withdraw", short_help="Withdraw staking two")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option(
    "-a",
    "--amount",
    help="withdraw staking XTWO, 0 will withdraw all staking",
    type=str,
    default="0",
    show_default=True
)
@click.option("-t", "--address", help="staking withdraw address", type=str, default="", show_default=True)
def staking_withdraw_cmd(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
    amount: str,
    address: str,
) -> None:
    extra_params = {
        "amount": amount,
        "address": address,
    }
    import asyncio
    from .wallet_funcs import execute_with_wallet, staking_withdraw

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, staking_withdraw))
