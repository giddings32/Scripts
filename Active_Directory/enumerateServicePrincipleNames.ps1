$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = ($domainObj.PdcRoleOwner).Name
$SearchString = "LDAP://"
$SearchString += $PDC + "/"
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$SearchString += $DistinguishedName
$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
$objDomain = New-Object System.DirectoryServices.DirectoryEntry
$Searcher.SearchRoot = $objDomain

# change name as needed

$Searcher.filter="serviceprincipalname=*http*" 
$Result = $Searcher.FindAll()
Foreach($obj in $Result)
{
 Foreach($prop in $obj.Properties)
 {
 $prop
 }


$SPN_initial = $prop.serviceprincipalname
$SPN = $SPN_initial.split("/")[1].split(":")[0]
Write-Host ""
Write-Host "Sam Account Name : [+]" $prop.samaccountname n
Write-Host "Service Principal Name : [+]" $SPN n
 
If ($SPN -like "*.com") {
nslookup $SPN
}

Write-Host "--------------------------------------------------------"
}
