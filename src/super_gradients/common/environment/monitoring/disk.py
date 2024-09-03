import psutil

from super_gradients.common.environment.monitoring.utils import bytes_to_megabytes

# Initialize the disk I/O counters safely
io_counters = psutil.disk_io_counters()
buffer_io_read_bytes = io_counters.read_bytes if io_counters is not None else 0
buffer_io_write_bytes = io_counters.write_bytes if io_counters is not None else 0

def get_disk_usage_percent() -> float:
    """Disk memory used in percent."""
    return psutil.disk_usage("/").percent

def get_io_read_mb() -> float:
    """Number of MegaBytes read since import"""
    io_counters = psutil.disk_io_counters()
    if io_counters is not None:
        return bytes_to_megabytes(io_counters.read_bytes - buffer_io_read_bytes)
    return 0  # Return 0 or handle it as needed

def get_io_write_mb() -> float:
    """Number of MegaBytes written since import"""
    io_counters = psutil.disk_io_counters()
    if io_counters is not None:
        return bytes_to_megabytes(io_counters.write_bytes - buffer_io_write_bytes)
    return 0  # Return 0 or handle it as needed

def reset_io_read():
    """Reset the value of net_io_counters"""
    global buffer_io_read_bytes
    io_counters = psutil.disk_io_counters()
    if io_counters is not None:
        buffer_io_read_bytes = io_counters.read_bytes

def reset_io_write():
    """Reset the value of net_io_counters"""
    global buffer_io_write_bytes
    io_counters = psutil.disk_io_counters()
    if io_counters is not None:
        buffer_io_write_bytes = io_counters.write_bytes
