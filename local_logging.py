import csv

def createLogEntry(options, username, servername, target, share, sharedFile, logFile):
    row = [
        username,
        servername,
        target.name,
        target.ip,
        share.shareName,
        sharedFile.fileName,
        sharedFile.fullPath,
        ("D" if sharedFile.isDirectory > 0 else ""),
        sharedFile.cTime,
        sharedFile.mTime,
        sharedFile.aTime,
        sharedFile.fileSize,
    ]
    writer = csv.writer(logFile)
    writer.writerow(row)
