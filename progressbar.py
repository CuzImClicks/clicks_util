
class ProgressBar:

    def __init__(self, length=10, prefix="", suffix=""):
        self.length = length
        self.prefix = prefix
        self.suffix = suffix
        self.current_value = 0

    def update(self, new_value):
        import sys
        percent = float(new_value) / self.length
        hashes = '#' * int(round(percent * self.length))
        spaces = "-" * (self.length - len(hashes))
        self.current_value = new_value
        sys.stdout.write(
            f"\r{self.prefix}: [{hashes + spaces}] {str(int(round(percent * 100))).zfill(2)}% | {self.suffix}")
        sys.stdout.flush()
        
    def get_length(self):
        return self.length
    
    def set_length(self, new_length):
        self.length = new_length
        
    def get_prefix(self):
        return self.prefix

    def set_prefix(self, new_prefix):
        self.prefix = new_prefix
        
    def get_suffix(self):
        return self.suffix
    
    def set_suffix(self, new_suffix):
        self.suffix = new_suffix
