import traceback
import logging

logger = logging.getLogger(__name__)


def wrap(pre, post):
    """Wrapper"""

    def decorate(func):
        """Decorator"""

        def call(*args, **kwargs):
            """Actual wrapping"""
            try:
                pre(func, args, kwargs)
                result = func(*args, **kwargs)
                post(func, result)
                return result
            except Exception as e:
                logger.exception(msg=traceback.format_exc())

        return call

    return decorate


def entering(func, args, kwargs):
    """Pre function logging"""
    logger.debug("Entered %s with args %s and kwargs %s", func.__name__, args, kwargs)


def exiting(func, result):
    """Post function logging"""
    logger.debug("Exited %s with result %s", func.__name__, result)
