<h1>Pexip Infinity in Azure</h1>

Button below deploys whole Pexip Infinity solution to Azure. That includes:

<p>-Image creation out of VHDs in Storage BLOBs</p>
<p>-NICs</p>
<p>-Management Node</p>
<p>-Availability Set</p>
<p>-selected number of Conference Nodes distributed across the Availability Set</p>

<b>Prereqs:</b>
So far you have to copy images to Storage Blobs and create VNET before you trigger this deployment. Other files in repo will not work so far but they will be part of nested deployment later. 

<h2>Kick it off!</h2>

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fmatousrokos%2FInfinity%2Fmaster%2FPexipInfinity%2FvMs.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
