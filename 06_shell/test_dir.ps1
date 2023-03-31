if (($args.Count -eq 1) -and (Test-Path $args[0]))
{
    $count=0
    $names=Get-ChildItem -Path $args[0] -Force
    foreach($n in $names)
    {
        Write-Host($n.Name)
        $count++
    }
Write-Host('Total:', $count)
}
else
{
    "Wrong number of arguments or directory does not exist"
}