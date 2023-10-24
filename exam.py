1#
function IPv4($ip) {
    $octets = $ip -split '.'
    if ($octets.Length -ne 4) {
        return $false
    }
    foreach ($octet in $octets) {
        $intValue = [int]$octet
        if ($intValue -lt 0 -or $intValue -gt 255) {
            return $false
        }
    }
    return $true
}
$ip = "192.168.0.1"
if (IPv4($ip)) {
    Write-Host "$ip is a valid IPv4 address."
} else {
    Write-Host "$ip is not a valid IPv4 address."



2#
#!/bin/bash


3#
def qq(string):
    words = string.split()
    reversed_words = [word[::-1] 
    if len(word) >= 5 else word for word in words]
    return ' '.join(reversed_words)

string = "Я календарь переверну, на фото я твое взгляну"
result = qq(string)
print(result)
