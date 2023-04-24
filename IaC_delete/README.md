### Scheduling Python scripts with GitHub Actions

In this scripts, I scheduled the deletion of infatructures from a cloud provider(Azure).

This can be very useful for labs and practice use cases, incase I forget to delete anything after a practice or lab. 

That way I do not incure added on costs on my credit :).

### Environments Variables

To run this script:


Add your `AZURE_CREDENTIALS` as a json object to github as secrets, as shown below:


{
  "clientId": "<your_client_id>",
  "clientSecret": "<your_client_secret>",
  "subscriptionId": "<your_subscription_id>",
  "tenantId": "<your_tenant_id>"
}


Check [here](https://geeksarray.com/blog/get-azure-subscription-tenant-client-id-client-secret) to see how to obtain AZURE_CREDENTIALS.