# encoding: utf-8
# module _thread
# from (built-in)
# by generator 1.145
"""
这个为编写多线程程序提供了一些原始操作（原语？）
threading 模块会提供更方便的接口
"""
# no imports

# Variables with simple values

TIMEOUT_MAX = 4294967.0

# functions

def allocate(): # real signature unknown; restored from __doc__
    """
    allocate_lock() -> lock object
    (allocate() 是一个过时的同义词，现在调用的都是下面的 allocate_lock() 函数)

    创建一个新的锁对象。
    执行 help(type(threading.Lock())) 这条语句可以获得更多关于锁对象的信息。
    """
    pass

def allocate_lock(): # real signature unknown; restored from __doc__
    """
    allocate_lock() -> lock object
    (allocate() 是一个过时的同义词，现在调用的都是下面的 allocate_lock() 函数)

    创建一个新的锁对象。
    执行 help(type(threading.Lock())) 这条语句可以获得更多关于锁对象的信息。
    """
    pass

def exit(): # real signature unknown; restored from __doc__
    """
    exit()
    (exit_thread() 是一个过时的同义词)

    这是 'raise SystemExit' 的同义词，
    它将导致当前线程悄无声息地退出，除非捕获了这个异常
    """
    pass

def exit_thread(): # real signature unknown; restored from __doc__
    """
    exit()
    (exit_thread() 是一个过时的同义词)

    这是 'raise SystemExit' 的同义词，
    它将导致当前线程悄无声息地退出，除非捕获了这个异常
    """
    pass

def get_ident(): # real signature unknown; restored from __doc__
    """
    get_ident() -> integer
    
    返回一个非零整数，该整数在同时存在的其他线程中唯一标识当前线程。
    这可用于标识每个线程的资源。
    即使在某些平台上，线程标识似乎是从1开始分配的连续数字，
    但不应依赖于此行为，而应将此数字纯粹视为一个神奇的cookie。
    一个线程的标识在退出后可以被另一个线程重用。
    （机翻）
    """
    return 0

def interrupt_main(): # real signature unknown; restored from __doc__
    """
    interrupt_main()
    
    在主线程引发键盘中断，
    子线程可以使用此函数中断主线程。
    """
    pass

def stack_size(size=None): # real signature unknown; restored from __doc__
    """
    stack_size([size]) -> size
    
    返回创建新线程时使用的线程堆栈大小。
    可选的size参数指定要用于后续创建的线程的堆栈大小（以字节为单位），
    并且必须为0（使用平台或配置的默认值）或至少为32768（32K）的正整数值。
    如果不支持更改线程堆栈大小，则会引发ThreadError异常。
    如果指定的大小无效，将引发ValueError异常，且堆栈大小不会被修改。
    当前支持的最小堆栈大小值为32K字节，以确保为解释器本身提供足够的堆栈空间。
    请注意，有些平台可能对堆栈大小的值有特定的限制，例如需要大于32KB的最小堆栈大小，
    或者需要以系统内存页面大小的倍数进行分配-有关详细信息，应参考平台文档
    （通常使用4KB的页面；如果没有更具体的信息，建议使用4096的倍数作为堆栈大小）。
    （机翻）
    """
    pass

def start_new(function, args, kwargs=None): # known case of _thread.start_new
    """
    start_new_thread(function, args[, kwargs])
    (start_new() 是一个过时的同义词)

    启动一个新线程并返回其标识符。
    线程将使用来自tuple参数的位置参数和来自字典kwargs的关键字参数调用函数。
    当函数返回时，线程退出；返回值被忽略。当函数引发未处理的异常时，线程也将退出；
    除非异常为SystemExit，否则将打印堆栈跟踪。 
    """
    return 0

def start_new_thread(function, args, kwargs=None): # real signature unknown; restored from __doc__
    """
    start_new_thread(function, args[, kwargs])
    (start_new() 是一个过时的同义词)

    启动一个新线程并返回其标识符。
    线程将使用来自tuple参数的位置参数和来自字典kwargs的关键字参数调用函数。
    当函数返回时，线程退出；返回值被忽略。当函数引发未处理的异常时，线程也将退出；
    除非异常为SystemExit，否则将打印堆栈跟踪。 
    """
    pass

def _count(): # real signature unknown; restored from __doc__
    """
    _count() -> integer
    
    返回当前运行的python线程数量，不包括主线程。
    这个数目包括了 start_new_thread() 和 threading.Thread 两种方式创建的线程。
    但这个函数尚未完工。

    此功能仅限于内部和特殊目的使用，
    在大多数应用程序中，应该改为使用 threading.enumerate() 这个函数
    """
    return 0

def _set_sentinel(): # real signature unknown; restored from __doc__
    """
    _set_sentinel() -> lock

    设置一个 sentinel 锁，当当前线程状态结束时（从解释器中解除后）释放该锁。
    这是 threading 模块的专用API。
    """
    pass

# classes

class error(Exception):
    """ Unspecified run-time error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class LockType(object):
    """
    锁是一个同步原语，要创建一个锁对象，请调用 threading.Lock()
    锁对象具有以下方法

    acquire() -- 上锁，可能会堵塞，直到获得锁为止
    release() -- 释放锁
    locked() -- 测试这个锁当前是否被锁上了（是否被线程获得）
    """
    def acquire(self, blocking=True, timeout=-1): # real signature unknown; restored from __doc__
        """
        acquire(blocking=True, timeout=-1) -> bool
        (acquire_lock() 是一个过时的同义词)

        当blocking=True，如果锁已被锁定（甚至被同一线程锁定），
        那么申请锁的线程就会被堵塞住，直到获得锁之后结束堵塞，并得到函数的返回值True。
        当blocking=False，即使锁已被锁定，
        申请锁的线程也不会被堵塞，而是立即获得返回值。
        函数的返回值表示是否成功获取到了锁，True/False
        堵塞操作可中断
        """
        return False

    def acquire_lock(self): # real signature unknown; restored from __doc__
        """
        acquire(blocking=True, timeout=-1) -> bool
        (acquire_lock() 是一个过时的同义词)
        
        当blocking=True，如果锁已被锁定（甚至被同一线程锁定），
        那么申请锁的线程就会被堵塞住，直到获得锁之后结束堵塞，并得到函数的返回值True。
        当blocking=False，即使锁已被锁定，
        申请锁的线程也不会被堵塞，而是立即获得返回值。
        函数的返回值表示是否成功获取到了锁，True/False
        堵塞操作可中断
        """
        pass

    def locked(self): # real signature unknown; restored from __doc__
        """
        locked() -> bool
        (locked_lock() 是一个过期的同义词)
        
        返回这个锁是否正处于锁定状态
        """
        return False

    def locked_lock(self): # real signature unknown; restored from __doc__
        """
        locked() -> bool
        (locked_lock() 是一个过期的同义词)
        
        返回这个锁是否正处于锁定状态
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        release()
        (release_lock() 是一个过期的同义词)

        释放锁，允许正在堵塞等待的其他进程获取这个锁，
        只有这个锁正处于锁定状态的时候才能调用这个函数。
        这里不要求上锁和释放锁的线程是同一个线程。
        """
        pass

    def release_lock(self): # real signature unknown; restored from __doc__
        """
        release()
        (release_lock() 是一个过期的同义词)

        释放锁，允许正在堵塞等待的其他进程获取这个锁，
        只有这个锁正处于锁定状态的时候才能调用这个函数。
        这里不要求上锁和释放锁的线程是同一个线程。
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """
        acquire(blocking=True, timeout=-1) -> bool
        (acquire_lock() 是一个过时的同义词)
        
        当blocking=True，如果锁已被锁定（甚至被同一线程锁定），
        那么申请锁的线程就会被堵塞住，直到获得锁之后结束堵塞，并得到函数的返回值True。
        当blocking=False，即使锁已被锁定，
        申请锁的线程也不会被堵塞，而是立即获得返回值。
        函数的返回值表示是否成功获取到了锁，True/False
        堵塞操作可中断
        """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """
        release()
        (release_lock() 是一个过期的同义词)

        释放锁，允许正在堵塞等待的其他进程获取这个锁，
        只有这个锁正处于锁定状态的时候才能调用这个函数。
        这里不要求上锁和释放锁的线程是同一个线程。
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class RLock(object):
    # no doc
    def acquire(self, blocking=True): # real signature unknown; restored from __doc__
        """
        acquire(blocking=True) -> bool

        上锁，
        当blocking=True，如果锁已被其他线程锁定，
        那么申请锁的线程就会被堵塞住，直到获得锁之后结束堵塞，并得到函数的返回值True。
        （但是，在同一线程内，对RLock进行多次acquire()操作，程序不会阻塞。）

        当blocking=False，即使锁已被锁定，
        申请锁的线程也不会被堵塞，而是立即获得返回值。
        函数的返回值表示是否成功获取到了锁，True/False
        （注意：堵塞操作是可中断的）

        准确地说，如果当前线程已经持有锁，则其内部计数器只会简单地递增。
        如果没有人持有该锁，则获取该锁并将其内部计数器初始化为1。
        """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """
        release()
        
        释放锁，
        只有当前锁处于锁定状态时才能调用这个函数。
        上锁和解锁的线程必须是同一个线程，否则将抛出 RuntimeError 异常。

        请注意，如果锁在当前线程中被多次 acquire() ，
        那么需要同样次数的执行释放才能真正释放这个锁
        """
        pass

    def _acquire_restore(self, state): # real signature unknown; restored from __doc__
        """
        _acquire_restore(state) -> None
        
        供 threading.Condition 内部使用。
        """
        pass

    def _is_owned(self): # real signature unknown; restored from __doc__
        """
        _is_owned() -> bool
        
        供 threading.Condition 内部使用。
        """
        return False

    def _release_save(self): # real signature unknown; restored from __doc__
        """
        _release_save() -> tuple
        
        供 threading.Condition 内部使用。
        """
        return ()

    def __enter__(self, *args, **kwargs): # real signature unknown
        """
        acquire(blocking=True) -> bool

        上锁，
        当blocking=True，如果锁已被其他线程锁定，
        那么申请锁的线程就会被堵塞住，直到获得锁之后结束堵塞，并得到函数的返回值True。
        （但是，在同一线程内，对RLock进行多次acquire()操作，程序不会阻塞。）

        当blocking=False，即使锁已被锁定，
        申请锁的线程也不会被堵塞，而是立即获得返回值。
        函数的返回值表示是否成功获取到了锁，True/False
        （注意：堵塞操作是可中断的）

        准确地说，如果当前线程已经持有锁，则其内部计数器只会简单地递增。
        如果没有人持有该锁，则获取该锁并将其内部计数器初始化为1。
        """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """
        release()
        
        释放锁，
        只有当前锁处于锁定状态时才能调用这个函数。
        上锁和解锁的线程必须是同一个线程，否则将抛出 RuntimeError 异常。

        请注意，如果锁在当前线程中被多次 acquire() ，
        那么需要同样次数的执行释放才能真正释放这个锁
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class _local(object):
    """ Thread-local data """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class __loader__(object):
    """
    内置模块的元路径引入（这个是什么？）
    
        所有方法都是静态方法或者类方法，以避免实例化一个类。
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

__spec__ = None # (!) real value is ''

