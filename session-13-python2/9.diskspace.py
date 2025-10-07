import shutil

total,used,free=shutil.disk_usage("/")
print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

#percentage Usage
print("Percentage Used: %d%%" % (used / total * 100))
print("Percentage Free: %d%%" % (free / total * 100))
print("Percentage Total: %d%%" % ((used+free) / total * 100))
