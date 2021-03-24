from trezor import loop, ui, wire

if __debug__:
    from apps.debug import confirm_signal

if False:
    from typing import Callable, List, Tuple, Optional, Any, Awaitable

CONFIRMED = object()
CANCELLED = object()
INFO = object()


def is_confirmed(x: Any) -> bool:
    return x is CONFIRMED


async def raise_if_cancelled(a: Awaitable, exc: Any = wire.ActionCancelled) -> None:
    result = await a
    if result is CANCELLED:
        raise exc


async def is_confirmed_info(
    ctx: wire.GenericContext,
    dialog: ui.Layout,
    info_func: Callable,
) -> bool:
    while True:
        result = await ctx.wait(dialog)

        if result is INFO:
            await info_func(ctx)
        else:
            return is_confirmed(result)


class ConfirmBase(ui.Layout):
    def __init__(
        self,
        content: ui.Component,
        confirm: Optional[ui.Component] = None,
        cancel: Optional[ui.Component] = None,
    ) -> None:
        self.content = content
        self.confirm = confirm
        self.cancel = cancel

    def dispatch(self, event: int, x: int, y: int) -> None:
        super().dispatch(event, x, y)
        self.content.dispatch(event, x, y)
        if self.confirm is not None:
            self.confirm.dispatch(event, x, y)
        if self.cancel is not None:
            self.cancel.dispatch(event, x, y)

    def on_confirm(self) -> None:
        raise ui.Result(CONFIRMED)

    def on_cancel(self) -> None:
        raise ui.Result(CANCELLED)

    if __debug__:

        def read_content(self) -> List[str]:
            return self.content.read_content()

        def create_tasks(self) -> Tuple[loop.Task, ...]:
            return super().create_tasks() + (confirm_signal(),)


class Pageable:
    def __init__(self) -> None:
        self._page = 0

    def page(self) -> int:
        return self._page

    def page_count(self) -> int:
        raise NotImplementedError

    def is_first(self) -> bool:
        return self._page == 0

    def is_last(self) -> bool:
        return self._page == self.page_count() - 1

    def next(self) -> None:
        self._page = min(self._page + 1, self.page_count() - 1)

    def prev(self) -> None:
        self._page = max(self._page - 1, 0)
