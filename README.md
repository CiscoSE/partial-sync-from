# Partial sync from

Action example that performs a partial sync-from on a given device from Cisco NSO. 

## Usage example

 ```
 admin@ncs(config)# partial-sync-from:action partial-sync-from device csr0 xpath ios:interface/GigabitEthernet[name=1]            

 ```

## NSO version

NSO 5.x

## Installation

1. Clone this repo on the NSO packages directory
2. cd partial-sync-from/src
3. make clean all
4. Reload packages in NSO

## Contacts

* Santiago Flores Kanter (sfloresk@cisco.com)

## License

Provided under Cisco Sample Code License, for details see [LICENSE](./LICENSE)

## Code of Conduct

Our code of conduct is available [here](./CODE_OF_CONDUCT.md)

## Contributing

See our contributing guidelines [here](./CONTRIBUTING.md)
