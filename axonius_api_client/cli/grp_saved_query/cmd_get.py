# -*- coding: utf-8 -*-
"""Command line interface for Axonius API Client."""
from __future__ import absolute_import, division, print_function, unicode_literals

import click

from .. import context
from . import grp_common


@click.command(name="get", context_settings=context.CONTEXT_SETTINGS)
@context.OPT_URL
@context.OPT_KEY
@context.OPT_SECRET
@context.OPT_EXPORT_FILE
@context.OPT_EXPORT_PATH
@context.OPT_EXPORT_FORMAT
@context.OPT_EXPORT_OVERWRITE
@context.OPT_MAX_ROWS
@context.pass_context
@click.pass_context
def cmd(
    clickctx,
    ctx,
    url,
    key,
    secret,
    export_format,
    export_file,
    export_path,
    export_overwrite,
    max_rows,
):
    """Get a report of adapters for objects in query."""
    client = ctx.start_client(url=url, key=key, secret=secret)

    api = getattr(client, clickctx.parent.parent.command.name)

    with context.exc_wrap(wraperror=ctx.wraperror):
        raw_data = api.saved_query.get(max_rows=max_rows)

    formatters = {"json": context.to_json, "csv": grp_common.to_csv}

    ctx.handle_export(
        raw_data=raw_data,
        formatters=formatters,
        export_format=export_format,
        export_file=export_file,
        export_path=export_path,
        export_overwrite=export_overwrite,
    )
