$LocalPath = "C:\Users\<USERNAME>\myexcel.xls"
$RemotePath = "\\<Remote_Workstation_IP>\c$\myexcel.xls"
[System.IO.File]::Copy($LocalPath, $RemotePath, $True)
