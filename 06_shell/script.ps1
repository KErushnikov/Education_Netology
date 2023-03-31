if ($args.Count -ne 2)
{
    "Wrong number of parameters for this script"
}
elseif (($null -ne $args[0]) -and ($null -ne $args[1]) -and ($args[0] -eq "crypt"))
{    
    "Encrypting..."
    [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($args[1]))
}
elseif (($null -ne $args[0]) -and ($null -ne $args[1]) -and ($args[0] -eq "decrypt"))
{
    "Decrypting..."
    [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($args[1]))
}   
else
{
   "Input correct method"
}