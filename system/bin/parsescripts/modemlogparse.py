#!/usr/bin/env python3
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import struct
import os

from config import *

def modem_boot_log_append(logpath):
    try:
        print ("begin modem_boot_log_append")
        father_path = os.path.abspath(logpath + os.path.sep + "..")
        father_path = os.path.abspath(father_path + os.path.sep + "..")
        modem_boot_path = os.path.join(father_path, "modem_log", "modem_boot_log.txt")
        if os.path.exists(modem_boot_path):
            modem_dump_path = os.path.join(logpath, modem_dump_txt)
            if os.path.exists(modem_dump_path):
                with open(modem_dump_path, "a") as modem_fs:
                    modem_fs.write(r"########### modem_boot_log ###########")
                with open(modem_dump_path, "ab") as modem_fs:
                    for line in open(modem_boot_path, "rb"):
                        modem_fs.write(line)
            else:
                with open(modem_dump_path, "wb+") as modem_fs:
                    for line in open(modem_boot_path, "rb"):
                        modem_fs.write(line)
            with open(modem_dump_path, "a") as modem_fs:
                modem_fs.write(r"########### modem_boot_log end ###########")
        else:
            print(modem_boot_path)
            print("modem_boot_log_path err")
    except (BaseException) as reason:
        print("modem_boot_log err")
        print(reason)
    except:
        print("err end")
        
def modem_kernel_log_append(logpath):
    try:
        print ("begin modem_kernel_log_append")
        print ("logpath: " + logpath)
        modem_kernel_print_log = logpath + modem_print
        print ("modem_kernel_print_log: " + modem_kernel_print_log)
        if os.path.exists(modem_kernel_print_log):
            modem_dump_path = os.path.join(logpath, modem_dump_txt)
            print ("modem_dump_path: " + modem_dump_path)
            if os.path.exists(modem_dump_path):
                with open(modem_dump_path, "a") as modem_fs:
                    modem_fs.write(r"########### phone_ap_print_log ###########")
                with open(modem_dump_path, "ab") as modem_fs:
                    for line in open(modem_kernel_print_log, "rb"):
                        modem_fs.write(line)
            else:
                with open(modem_dump_path, "wb+") as modem_fs:
                    for line in open(modem_kernel_print_log, "rb"):
                        modem_fs.write(line)
            with open(modem_dump_path, "a") as modem_fs:
                modem_fs.write(r"########### phone_ap_print_log end ###########")
        else:
            print(modem_kernel_print_log)
            print("modem_kernel_print_log err1")
    except (BaseException) as reason:
        print("modem_kernel_print_log err2")
        print(reason)
    except:
        print("modem_kernel_print_log err2 end")

def dump_backup_bin_parse(logpath):
    outfile = os.path.join(logpath, modem_dump_txt)
    filename = 'modem_dump'
    infile = logpath + modem_back
    print ("dump_backup_bin_parse  begin\n")
    print(("infile: " + infile))
    print(("outfile: " + outfile))
    if not os.path.exists(outfile):
        import_file = 'import ' + filename + '_parser'
        function = 'ret = ' + filename + '_parser' + '.' + 'entry_' + filename + '_parser' + '(infile, outfile)'
        print(("import_file: " + import_file))
        print(("function: " + function))
        exec(import_file)
        exec(function)
    else :
        print ("file exit")    
    print ("dump_backup_bin_parse  begin\n")

def modemlogparse(logpath):
    ret = 0
    if logpath == "all":
        rootdir = '/data/hisi_logs/'
        if os.path.exists(rootdir):
            try:
                dirs = os.listdir(rootdir)
                print(dirs)
                for dirc in dirs:
                    if os.path.isdir(rootdir + dirc) and dirc[:8].isdigit():
                        dirtoparse = '%s%s%s' %(rootdir, dirc, '/cp_log/')
                        if os.path.exists(dirtoparse):
                            try:
                                parsesinglepath(dirtoparse)
                            except (BaseException) as reason:
                                print(reason)
                            except:
                                print("parse err")
                            #dump_backup_bin_parse(dirtoparse)
                            modem_boot_log_append(dirtoparse)
                            modem_kernel_log_append(dirtoparse)
            except (BaseException) as reason:
                print(reason)
            except:
                print("permit err")
        else:
            print("dir not exists")
    else:
        if os.path.exists(logpath):
            try:
                parsesinglepath(logpath)
            except (BaseException) as reason:
                print(reason)
            except:
                print("parse err")
            #dump_backup_bin_parse(logpath)
            modem_boot_log_append(logpath)
            modem_kernel_log_append(logpath)

    return ret


def parselinkedfile(in_handler, logpath):
    in_handler.seek(0,2)
    linkfilelen = in_handler.tell()
    print("linkfilelen is %d" % linkfilelen)
    in_handler.seek(0)
    curpos = 0
    while in_handler.tell() < linkfilelen:
        magic,=struct.unpack("I", in_handler.read(4))

        if 0x56786543 == magic:
            magic2,=struct.unpack("I", in_handler.read(4))
            linkfilename = in_handler.readline(32)
            print(linkfilename)
            linkfilename = linkfilename.decode(encoding="utf-8").strip('\x00')
            print(linkfilename)
            dstfilename, = struct.unpack('32s',in_handler.read(32))
            filenum, =struct.unpack("I", in_handler.read(4))
            totalnum, =struct.unpack("I", in_handler.read(4))
            packetnum, =struct.unpack("I", in_handler.read(4))
            totalpacket, =struct.unpack("I", in_handler.read(4))
            filelength, =struct.unpack("I", in_handler.read(4))
            realLength, =struct.unpack("I", in_handler.read(4))
            isAppend, =struct.unpack("I", in_handler.read(4))
            maxLength, =struct.unpack("I", in_handler.read(4))

            print("linked file is %s " % linkfilename)
            (filename,extension) = os.path.splitext(linkfilename)
            outfile = '%s%s%s' %(logpath, filename, '.txt')
            offset = in_handler.tell()

            if linkfilename in list(filedict.keys()):
                import_file = '%s%s%s' %('import ', filename, '_parser')
                function = '%s%s%s%s%s%s%s%s' %('ret = ', filename, '_parser', '.', 'entry_', filename, '_parser_link', '(in_handler, outfile, offset, filelength)')
                print(import_file)
                print(function)
                exec(import_file)
                exec(function)
            else:
                print("file %s not in the list" % linkfilename)
            curpos = curpos + int(filelength) + 104
            print("curpos is 0x%x" % curpos)
            in_handler.seek(curpos)
        else:
            break
    return


def parsesinglepath(logpath):
    ret = 0
    if os.path.exists(logpath + "DONE"):
        print('this directory already parse done')
        return ret

    for filetoparse in list(filedict.keys()):
        infile =  '%s%s' %(logpath, filetoparse)
        outfile = '%s%s' %(logpath, filedict[filetoparse])
        print(infile)
        print(outfile)

        if os.path.exists(infile):
            (filename,extension) = os.path.splitext(filetoparse)
            with open(infile,"rb") as in_handler:
                magic,=struct.unpack("I", in_handler.read(4))
                print("magic is %d" % magic)
                if 0x56786543 == magic:
                    parselinkedfile(in_handler, logpath)
                    os.mknod(logpath + "DONE")
                    in_handler.close()
                    return
                else:
                    in_handler.close
                    print("oldstyle\n")
                    import_file = '%s%s%s' %('import ', filename, '_parser')
                    function = '%s%s%s%s%s%s%s%s' %('ret = ', filename, '_parser', '.', 'entry_', filename, '_parser', '(infile, outfile)')
                    exec(import_file)
                    exec(function)
                    ret = 0
        else:
            print((infile + "is not existed"))
            ret  = 0
    if ret == 0:
        os.mknod(logpath + "DONE")
    return




def main():
    if len(sys.argv) < 2:
        print("invalid argument")
        return
    else:
        logpath = sys.argv[1]

    for filetoparse in list(filedict.keys()):
        infile =  logpath + filetoparse
        outfile = logpath + filedict[filetoparse]
        print(("infile: " + infile))
        print(("outfile: " + outfile))


        if os.path.exists(infile):
            (filename,extension) = os.path.splitext(filetoparse)
            with open(infile,"rb") as in_handler:

                magic,=struct.unpack("I", in_handler.read(4))
                print("magic is %d" % magic)
                if 0x56786543 == magic:
                    parselinkedfile(in_handler, logpath)
                    in_handler.close()
                    return
                else:
                    in_handler.close
                    print("oldstyle\n")
                    import_file = '%s%s%s' %('import ', filename, '_parser')
                    function = '%s%s%s%s%s%s%s%s' %('ret = ', filename, '_parser', '.', 'entry_', filename, '_parser', '(infile, outfile)')
                    exec(import_file)
                    exec(function)
                    ret = 0
        else:
            print((infile + "is not existed"))
            ret  = 1
    #dump_backup_bin_parse(logpath)
    modem_boot_log_append(logpath)
    modem_kernel_log_append(logpath)
    if ret == 0:
        os.mknod(logpath + "DONE")


if __name__ == '__main__':
    main()

