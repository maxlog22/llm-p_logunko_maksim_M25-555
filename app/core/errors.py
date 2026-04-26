class AppError(Exception):
    """Base application error."""


class ConflictError(AppError):
    """Raised when an object already exists."""


class UnauthorizedError(AppError):
    """Raised when authentication fails."""


class ForbiddenError(AppError):
    """Raised when access is denied."""


class NotFoundError(AppError):
    """Raised when an object does not exist."""


class ExternalServiceError(AppError):
    """Raised when an external service call fails."""