from ftplib import FTP
import getpass
import sys

def ftp_upload(server, username, password, local_path, remote_path):
    try:
        with FTP(server) as ftp:
            # 登录FTP服务器
            ftp.login(username, password)
            
            # 设置二进制传输模式
            ftp.voidcmd('TYPE I')
            
            # 上传文件
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
                
            print(f"文件 {local_path} 成功上传至 {remote_path}")
            
    except Exception as e:
        print(f"上传失败: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # 通过命令行参数获取输入
    server = input("FTP服务器地址: ")
    username = input("用户名: ")
    password = getpass.getpass("密码: ")
    local_path = input("本地文件路径: ")
    remote_path = input("远程路径: ")
    
    ftp_upload(server, username, password, local_path, remote_path)
