from typing import Any

import numpy as np
from typing_extensions import Self

from pandas._typing import (
    ArrayLike,
    Scalar,
    TakeIndexer,
    npt,
)

from pandas.core.dtypes.dtypes import ExtensionDtype

class ExtensionArray:
    def __getitem__(self, item) -> Any: ...
    def __setitem__(self, key: int | slice | np.ndarray, value: Self) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __contains__(self, item: object) -> bool | np.bool_: ...
    def to_numpy(
        self,
        dtype: npt.DTypeLike | None = ...,
        copy: bool = ...,
        na_value: Scalar = ...,
    ) -> np.ndarray: ...
    @property
    def dtype(self) -> ExtensionDtype: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    @property
    def ndim(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    def astype(self, dtype, copy: bool = ...): ...
    def isna(self) -> ArrayLike: ...
    def argsort(
        self, *, ascending: bool = ..., kind: str = ..., **kwargs
    ) -> np.ndarray: ...
    def fillna(self, value=..., method=..., limit=...): ...
    def dropna(self): ...
    def shift(self, periods: int = ..., fill_value: object = ...) -> Self: ...
    def unique(self): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    # TODO: remove keyword-only when pandas removed na_sentinel
    def factorize(self, *, use_na_sentinel: bool = ...) -> tuple[np.ndarray, Self]: ...
    def repeat(self, repeats, axis=...): ...
    def take(
        self,
        indexer: TakeIndexer,
        *,
        allow_fill: bool = ...,
        fill_value=...,
    ) -> Self: ...
    def copy(self) -> Self: ...
    def view(self, dtype=...) -> Self | np.ndarray: ...
    def ravel(self, order=...) -> Self: ...
    def tolist(self) -> list: ...

class ExtensionOpsMixin:
    @classmethod
    def _add_arithmetic_ops(cls) -> None: ...
    @classmethod
    def _add_comparison_ops(cls) -> None: ...
    @classmethod
    def _add_logical_ops(cls) -> None: ...

class ExtensionScalarOpsMixin(ExtensionOpsMixin): ...
