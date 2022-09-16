$com = [activator]::CreateInstance([type]::GetTypeFromProgId("Excel.Application", "<Remote_Workstation_IP>"))

$LocalPath = "C:\Users\<USERNAME>\myexcel.xls"

$RemotePath = "\\<Remote_Workstation_IP>\c$\myexcel.xls"

[System.IO.File]::Copy($LocalPath, $RemotePath, $True)

$Path = "\\<Remote_Workstation_IP>\c$\Windows\sysWOW64\config\systemprofile\Desktop"

$temp = [system.io.directory]::createDirectory($Path)

$Workbook = $com.Workbooks.Open("C:\myexcel.xls")

$com.Run("mymacro")
