"""
Conceptual VFS implementation showing interception pattern.
"""

class VirtualFileSystem:
    """Intercept file operations for controlled access."""
    
    def __init__(self):
        self.mounts = {}
        
    def mount(self, path, fetcher):
        """Mount a path to an external fetcher."""
        self.mounts[path] = fetcher
        
    def read(self, path):
        """Read file, potentially from remote source."""
        for mount_path, fetcher in self.mounts.items():
            if path.startswith(mount_path):
                relative = path[len(mount_path):]
                return fetcher(relative)
        raise FileNotFoundError(path)

# Example usage
vfs = VirtualFileSystem()
vfs.mount('/api/', lambda p: fetch_from_api(p))
vfs.mount('/local/', lambda p: read_local_cache(p))
