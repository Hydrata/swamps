import json

biocollect_response = json.loads('''{
    "data": {
        "searchBioCollectProject": [
            {
                "projectId": "f72f7cbc-5ccd-480f-8a4c-0a9a3a5c9cae",
                "activities": [
                    {
                        "activityId": "56b95f49-0e04-4581-a5e3-9dc58782b344",
                        "dateCreated": "2021-06-09",
                        "description": null,
                        "outputs": [
                            {
                                "name": "ACT Waterwatch - Water Bug Survey",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": 50,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "Other (specify in notes)",
                                            "key": "idConfirmedBy"
                                        },
                                        {
                                            "value": "4",
                                            "key": "taxaRichness"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "surveyDate"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": "This is a dummy data recording - please do not include in final results analysis.",
                                            "key": "eventRemarks"
                                        },
                                        {
                                            "value": "Fair",
                                            "key": "streamQualityRating"
                                        },
                                        {
                                            "value": "Sampled by university researchers",
                                            "key": "observationRemarks"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "taxonSensitivityClass": "Very Sensitive",
                                                    "taxonIndexValue": 10,
                                                    "individualCount": 2,
                                                    "taxonWeightFactor": 1,
                                                    "taxonName": {
                                                        "commonName": "Scorpion flies",
                                                        "outputSpeciesId": "c7e0b03a-ac3f-4559-b300-5abdc15045fd",
                                                        "scientificName": "Mecoptera",
                                                        "name": "Scorpion flies (Mecoptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:67c46151-7449-407a-a8b3-a283ba3f0771"
                                                    },
                                                    "taxonSensitivityRating": "10"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Sensitive",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Stoneflies",
                                                        "outputSpeciesId": "9dfe11ba-60e4-4ead-81b5-596be60be6fd",
                                                        "scientificName": "Plecoptera",
                                                        "name": "Stoneflies (Plecoptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:4fbe14c4-2efb-4874-8842-f29e05a93f92"
                                                    },
                                                    "taxonSensitivityRating": "10"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Sensitive",
                                                    "taxonIndexValue": 9,
                                                    "individualCount": 2,
                                                    "taxonWeightFactor": 1,
                                                    "taxonName": {
                                                        "commonName": "May flies",
                                                        "outputSpeciesId": "db51ca40-0a92-40df-b928-0cd834468f69",
                                                        "scientificName": "Ephemeroptera",
                                                        "name": "May flies (Ephemeroptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:928c5312-17a2-4557-b523-d207cacc332b"
                                                    },
                                                    "taxonSensitivityRating": "9"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Sensitive",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Alder flies",
                                                        "outputSpeciesId": "f42d28e0-3bfa-41d1-8b69-64f9e9882ef8",
                                                        "scientificName": "Megaloptera",
                                                        "name": "Alder flies (Megaloptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:1764aba8-641d-4eb8-ade5-ff33efafb054"
                                                    },
                                                    "taxonSensitivityRating": "8"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Sensitive",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Caddis flies",
                                                        "outputSpeciesId": "0435df81-4ac7-4382-ab3c-e7c74ca556ab",
                                                        "scientificName": "Trichoptera",
                                                        "name": "Caddis flies (Trichoptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:0964bf51-f620-4a71-9ab3-ff631f2099bb"
                                                    },
                                                    "taxonSensitivityRating": "8"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Sensitive",
                                                    "taxonIndexValue": 6,
                                                    "individualCount": 1,
                                                    "taxonWeightFactor": 1,
                                                    "taxonName": {
                                                        "commonName": "Horsehair worms; gordian worms",
                                                        "outputSpeciesId": "cd7d5b92-9b6f-414b-81c0-0c7546ca71a9",
                                                        "scientificName": "Nematomorpha",
                                                        "name": "Horsehair worms; gordian worms (Nematomorpha)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:4b1dd080-6a02-48c4-9f6c-94680f7651dd"
                                                    },
                                                    "taxonSensitivityRating": "6"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Sensitive",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Mites",
                                                        "outputSpeciesId": "cb192f53-d031-4349-b3c0-330fb86203ff",
                                                        "scientificName": "Acarina",
                                                        "name": "Mites (Acarina)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:c731c9bb-6292-4071-873d-2e8543dd120f"
                                                    },
                                                    "taxonSensitivityRating": "6"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Sensitive",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Cave shrimp",
                                                        "outputSpeciesId": "150e54fe-fd39-4a78-b460-7d0e8717a4e3",
                                                        "scientificName": "Anaspidacea",
                                                        "name": "Cave shrimp (Anaspidacea)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:5b4de720-d042-47b3-824a-542b12e7c771"
                                                    },
                                                    "taxonSensitivityRating": "6"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Sensitive",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Lacewings",
                                                        "outputSpeciesId": "35f56111-fb04-490a-965d-3ea9ee3c4356",
                                                        "scientificName": "Neuroptera",
                                                        "name": "Lacewings (Neuroptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:db09c273-56ae-4ef9-a5ed-53027aa7c63e"
                                                    },
                                                    "taxonSensitivityRating": "6"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": 10,
                                                    "individualCount": 3,
                                                    "taxonWeightFactor": 2,
                                                    "taxonName": {
                                                        "commonName": "Beetles - Riffle beetles, Whirligigs",
                                                        "outputSpeciesId": "edb2385c-9570-4069-80f1-882c7fb80d6c",
                                                        "scientificName": "Coleoptera",
                                                        "name": "Beetles - Riffle beetles, Whirligigs (Coleoptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:5c387616-0cb4-42f0-936e-7ec22d576939"
                                                    },
                                                    "taxonSensitivityRating": "5"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Freshwater sponges",
                                                        "outputSpeciesId": "18cc6435-7ed7-4586-a8c9-0b585b98719e",
                                                        "scientificName": "Porifera",
                                                        "name": "Freshwater sponges (Porifera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:ed334702-b153-41b0-ac93-e6aa4964331c"
                                                    },
                                                    "taxonSensitivityRating": "4"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Pipe-mosses",
                                                        "outputSpeciesId": "4003390b-a623-46c1-bb6d-7c5d86eb38d4",
                                                        "scientificName": "Bryozoa",
                                                        "name": "Pipe-mosses (Bryozoa)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:a1f069f9-eaa8-487c-889a-d3cfb3dd936e"
                                                    },
                                                    "taxonSensitivityRating": "4"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Yabbies; crayfish, shrimp",
                                                        "outputSpeciesId": "bd3e0215-b25b-465f-abc1-e9f938490eb2",
                                                        "scientificName": "Decapoda",
                                                        "name": "Yabbies; crayfish, shrimp (Decapoda)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:2f12112b-d593-4392-a9db-4b026b8805a3"
                                                    },
                                                    "taxonSensitivityRating": "4"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Aquatic millipedes",
                                                        "outputSpeciesId": "e405e51a-5a2a-4b32-badc-0cbc140fa945",
                                                        "scientificName": "Diplopoda",
                                                        "name": "Aquatic millipedes (Diplopoda)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:0a08c6cb-7990-4124-ac83-9d44274d6a84"
                                                    },
                                                    "taxonSensitivityRating": "4"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Proboscis worms",
                                                        "outputSpeciesId": "e477d064-c110-42d6-b080-d4c1a82e509c",
                                                        "scientificName": "Nemertea",
                                                        "name": "Proboscis worms (Nemertea)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:89e92ab7-7ffc-4cc4-9149-19c8f8079940"
                                                    },
                                                    "taxonSensitivityRating": "3"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Nematodes, roundworms",
                                                        "outputSpeciesId": "b0afdbdb-251e-4e32-b118-a165f344858c",
                                                        "scientificName": "Nematoda",
                                                        "name": "Nematodes, roundworms (Nematoda)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:0e7e0f7d-4456-495b-b762-2d11f78b9368"
                                                    },
                                                    "taxonSensitivityRating": "3"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Freshwater mussels; clams",
                                                        "outputSpeciesId": "5eb34e9f-6470-4ede-9186-18e5f2dc87f4",
                                                        "scientificName": "Bivalvia",
                                                        "name": "Freshwater mussels; clams (Bivalvia)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:8c3070f6-9475-4b6a-95cb-8afb944ad3d5"
                                                    },
                                                    "taxonSensitivityRating": "3"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Side-swimmers; scuds",
                                                        "outputSpeciesId": "f950afb4-65c2-4c7e-95c4-6872520dd8fd",
                                                        "scientificName": "Amphipoda",
                                                        "name": "Side-swimmers; scuds (Amphipoda)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:c799e373-f43a-446d-b2d0-836e6be97b84"
                                                    },
                                                    "taxonSensitivityRating": "3"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Fly larva - mosquito larvae, bloodworms",
                                                        "outputSpeciesId": "e2a1b363-c009-4355-896b-0f78c9847997",
                                                        "scientificName": "Diptera",
                                                        "name": "Fly larva - mosquito larvae, bloodworms (Diptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:933b2bf6-deee-4fd9-b669-4bf8cf7cc9ce"
                                                    },
                                                    "taxonSensitivityRating": "3"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Moderately Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Dragonfly; damselflies",
                                                        "outputSpeciesId": "01eaf704-2bb0-4e89-9190-9451723f4cb9",
                                                        "scientificName": "Odonata",
                                                        "name": "Dragonfly; damselflies (Odonata)",
                                                        "guid": "NZOR-4-24409"
                                                    },
                                                    "taxonSensitivityRating": "3"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Flatworms",
                                                        "outputSpeciesId": "b5af4c1d-1102-4618-b426-f5d3f96a05af",
                                                        "scientificName": "Turbellaria",
                                                        "name": "Flatworms (Turbellaria)",
                                                        "guid": "13010000"
                                                    },
                                                    "taxonSensitivityRating": "2"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Segmented worms",
                                                        "outputSpeciesId": "3c11c1a1-709f-4a00-ac77-ef7a7287ef4b",
                                                        "scientificName": "Oligochaeta",
                                                        "name": "Segmented worms (Oligochaeta)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:406916d5-9058-4d72-9dbf-d3f689e8f3b2"
                                                    },
                                                    "taxonSensitivityRating": "2"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Freshwater Slaters",
                                                        "outputSpeciesId": "a7953f8b-3137-44a2-a03f-88aeb7b71446",
                                                        "scientificName": "Isopoda",
                                                        "name": "Freshwater Slaters (Isopoda)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:e4720a22-d642-44c7-abc6-fb5b34d5e057"
                                                    },
                                                    "taxonSensitivityRating": "2"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "True bugs - backswimmers, water boatman, needle bugs",
                                                        "outputSpeciesId": "f72f0019-85ef-4215-82cf-3eea8693adfa",
                                                        "scientificName": "Hemiptera",
                                                        "name": "True bugs - backswimmers, water boatman, needle bugs (Hemiptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:7630fe33-a00e-4743-80da-4fa6a36cd8b2"
                                                    },
                                                    "taxonSensitivityRating": "2"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Moth larvae",
                                                        "outputSpeciesId": "bfa03624-0270-4ea0-bb04-42a11bce1fd5",
                                                        "scientificName": "Lepidoptera",
                                                        "name": "Moth larvae (Lepidoptera)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:7cb6c81c-a7c4-4dd5-8578-fcfd2de847d6"
                                                    },
                                                    "taxonSensitivityRating": "2"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Hydras",
                                                        "outputSpeciesId": "95257c70-d721-40a4-874f-11a4f695e587",
                                                        "scientificName": "Hydrozoa",
                                                        "name": "Hydras (Hydrozoa)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:40e34a43-accb-48e3-9492-09c39ac5f756"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Freshwater Snails",
                                                        "outputSpeciesId": "24ec2613-0e09-4bd4-8032-3364107e6569",
                                                        "scientificName": "Gastropoda",
                                                        "name": "Freshwater Snails (Gastropoda)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:ab81c7fc-3fc3-4e54-b277-a12a1a9cd0d8"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Leeches",
                                                        "outputSpeciesId": "e8d5002f-0284-4493-92df-727260cf6ecd",
                                                        "scientificName": "Hirudinea",
                                                        "name": "Leeches (Hirudinea)",
                                                        "guid": "22300000"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Bristleworms",
                                                        "outputSpeciesId": "3d8029c8-14b7-45cc-999c-a9ff16e97e78",
                                                        "scientificName": "Polychaeta",
                                                        "name": "Bristleworms (Polychaeta)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:d1251470-e6f7-4f43-b97d-276dab41b06b"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Brine shrimps; fairy shrimps",
                                                        "outputSpeciesId": "08c6f3a5-1528-46da-af6f-94ce75d4bf35",
                                                        "scientificName": "Anostraca",
                                                        "name": "Brine shrimps; fairy shrimps (Anostraca)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:dbc4f4ad-0ad5-4813-9275-95b00b448832"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Fish lice",
                                                        "outputSpeciesId": "60f31911-0fd4-43f1-8804-e748876d3313",
                                                        "scientificName": "Branchiura",
                                                        "name": "Fish lice (Branchiura)",
                                                        "guid": "NZOR-4-111042"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Clam shrimps",
                                                        "outputSpeciesId": "9bbdee1b-63dc-4e44-8dac-f05c3d8ca945",
                                                        "scientificName": "Cyclestheriidae",
                                                        "name": "Clam shrimps (Cyclestheriidae)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:925a4c2a-19fe-43c9-af4c-9b420b85b13a"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Tadpole shrimp",
                                                        "outputSpeciesId": "107afd11-0dea-4e02-bb59-25577be0cb5f",
                                                        "scientificName": "Notostraca",
                                                        "name": "Tadpole shrimp (Notostraca)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:7d0c7db7-6e86-4c63-bb4c-ca80c1b84a06"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                },
                                                {
                                                    "taxonSensitivityClass": "Very Tolerant",
                                                    "taxonIndexValue": "",
                                                    "individualCount": 0,
                                                    "taxonWeightFactor": 0,
                                                    "taxonName": {
                                                        "commonName": "Springtails",
                                                        "outputSpeciesId": "4fc0f0df-9334-4fb1-9fee-37270ec021c8",
                                                        "scientificName": "Collembola",
                                                        "name": "Springtails (Collembola)",
                                                        "guid": "urn:lsid:biodiversity.org.au:afd.taxon:53e5e456-0d08-4cff-ac1f-d453b2c07e3b"
                                                    },
                                                    "taxonSensitivityRating": "1"
                                                }
                                            ],
                                            "key": "taxaObservations"
                                        },
                                        {
                                            "value": "7",
                                            "key": "spiValue"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": "12:12 PM",
                                            "key": "surveyTime"
                                        },
                                        {
                                            "value": "0.3",
                                            "key": "surveyDuration"
                                        },
                                        {
                                            "value": "No",
                                            "key": "gambusiaPresent"
                                        },
                                        {
                                            "value": 150.3196666343577,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "riffle": true,
                                                    "habitatType": "Silt and sand"
                                                }
                                            ],
                                            "key": "habitatSampled"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.662904270303585,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": [
                                                "Sweep"
                                            ],
                                            "key": "samplingMethod"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "a07efb42-6b1d-4e91-8d98-c09b36a9c961",
                        "dateCreated": "2021-05-20",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Piezometer Readings",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "6.82",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": "Google maps",
                                            "key": "locationSource"
                                        },
                                        {
                                            "value": "68",
                                            "key": "waterDissolvedOxygenInPercentSaturation"
                                        },
                                        {
                                            "value": "Dr Ian Wright",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": "GCP1",
                                            "key": "piezometerId"
                                        },
                                        {
                                            "value": "6",
                                            "key": "waterPh"
                                        },
                                        {
                                            "value": "15.3",
                                            "key": "waterTemperatureInDegreesCelcius"
                                        },
                                        {
                                            "value": "0",
                                            "key": "waterTableHeightInCentimetres"
                                        },
                                        {
                                            "value": "25.8",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre"
                                        },
                                        {
                                            "value": 150.31964272901396,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": "11:00 AM",
                                            "key": "eventTime"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.66397758593848,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": "3",
                                            "key": "dipDuration"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "9042ff95-dd10-4c21-8661-5af072380813",
                        "dateCreated": "2021-06-09",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Piezometer Readings",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "3",
                                            "key": "dipDurationInMinutes"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": "Readings were taken by Dr Ian Wright and recorded / uploaded to BioCollect by Sarah Terkes",
                                            "key": "eventRemarks"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": "GCP1",
                                            "key": "piezometerId"
                                        },
                                        {
                                            "value": "216",
                                            "key": "totalWaterDepthInCentimetres"
                                        },
                                        {
                                            "value": "31",
                                            "key": "waterTableHeightInCentimetres"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "waterPh": "5.55",
                                                    "waterTemperatureInDegreesCelcius": "15.6",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "25.8",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "6.91",
                                                    "waterDissolvedOxygenInPercentSaturation": "68.9"
                                                },
                                                {
                                                    "waterPh": "5.56",
                                                    "waterTemperatureInDegreesCelcius": "15.3",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "25.8",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "6.86",
                                                    "waterDissolvedOxygenInPercentSaturation": "68.6"
                                                },
                                                {
                                                    "waterPh": "5.57",
                                                    "waterTemperatureInDegreesCelcius": "15.2",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "25.8",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "6.81",
                                                    "waterDissolvedOxygenInPercentSaturation": "68"
                                                },
                                                {
                                                    "waterPh": "5.57",
                                                    "waterTemperatureInDegreesCelcius": "15.3",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "25.8",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "6.81",
                                                    "waterDissolvedOxygenInPercentSaturation": "68"
                                                },
                                                {
                                                    "waterPh": "5.57",
                                                    "waterTemperatureInDegreesCelcius": "15.3",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "25.8",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "6.8",
                                                    "waterDissolvedOxygenInPercentSaturation": "67.9"
                                                }
                                            ],
                                            "key": "waterMeasurementsRepeatSection"
                                        },
                                        {
                                            "value": 150.31964272901396,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": "11:00 AM",
                                            "key": "eventTime"
                                        },
                                        {
                                            "value": "41",
                                            "key": "piezometerHeightAboveGroundInCentimetres"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.66397758593848,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": 10,
                                            "key": "relativeWaterLevelDifferenceInCentimetres"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "dde120bc-11be-437b-984c-48644c78552f",
                        "dateCreated": "2021-06-09",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Piezometer Readings",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "0",
                                            "key": "dipDurationInMinutes"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": "There is no piezometer at the exit stream so we just record the water physics here.",
                                            "key": "eventRemarks"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": "GCp2",
                                            "key": "piezometerId"
                                        },
                                        {
                                            "value": "0",
                                            "key": "totalWaterDepthInCentimetres"
                                        },
                                        {
                                            "value": "0",
                                            "key": "waterTableHeightInCentimetres"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "waterPh": "6.63",
                                                    "waterTemperatureInDegreesCelcius": "13.7",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "23.39",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "9.61",
                                                    "waterDissolvedOxygenInPercentSaturation": "92.6"
                                                },
                                                {
                                                    "waterPh": "6.62",
                                                    "waterTemperatureInDegreesCelcius": "13.7",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "23.41",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "9.61",
                                                    "waterDissolvedOxygenInPercentSaturation": "92.6"
                                                },
                                                {
                                                    "waterPh": "6.62",
                                                    "waterTemperatureInDegreesCelcius": "13.7",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "23.45",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "9.61",
                                                    "waterDissolvedOxygenInPercentSaturation": "9.61"
                                                },
                                                {
                                                    "waterPh": "6.62",
                                                    "waterTemperatureInDegreesCelcius": "13.7",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "23.42",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "9.61",
                                                    "waterDissolvedOxygenInPercentSaturation": "92.6"
                                                },
                                                {
                                                    "waterPh": "6.62",
                                                    "waterTemperatureInDegreesCelcius": "13.7",
                                                    "waterElectricalConductivityInMicrosiemensPerCentimetre": "23.37",
                                                    "waterDissolvedOxygenInMilligramsPerLitre": "9.61",
                                                    "waterDissolvedOxygenInPercentSaturation": "92.6"
                                                }
                                            ],
                                            "key": "waterMeasurementsRepeatSection"
                                        },
                                        {
                                            "value": 150.3196666343577,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": "01:10 PM",
                                            "key": "eventTime"
                                        },
                                        {
                                            "value": "0",
                                            "key": "piezometerHeightAboveGroundInCentimetres"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.662904270303585,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": 0,
                                            "key": "relativeWaterLevelDifferenceInCentimetres"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "532235bb-36c6-4155-98ed-73ae893fa2d7",
                        "dateCreated": "2021-06-11",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Piezometer Readings",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": "Data was recorded by Dr Ian Wright and Sarah Terkes",
                                            "key": "eventRemarks"
                                        },
                                        {
                                            "value": "15.6",
                                            "key": "waterTemperatureInDegreesCelcius_1"
                                        },
                                        {
                                            "value": "15.2",
                                            "key": "waterTemperatureInDegreesCelcius_3"
                                        },
                                        {
                                            "value": "15.3",
                                            "key": "waterTemperatureInDegreesCelcius_2"
                                        },
                                        {
                                            "value": "15.3",
                                            "key": "waterTemperatureInDegreesCelcius_5"
                                        },
                                        {
                                            "value": "15.3",
                                            "key": "waterTemperatureInDegreesCelcius_4"
                                        },
                                        {
                                            "value": "GCP1",
                                            "key": "piezometerId"
                                        },
                                        {
                                            "value": "216",
                                            "key": "totalWaterDepthInCentimetres"
                                        },
                                        {
                                            "value": "25.8",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_5"
                                        },
                                        {
                                            "value": "31",
                                            "key": "waterTableHeightInCentimetres"
                                        },
                                        {
                                            "value": "11:00 AM",
                                            "key": "eventTime"
                                        },
                                        {
                                            "value": "5.56",
                                            "key": "waterPh_2"
                                        },
                                        {
                                            "value": "68.6",
                                            "key": "waterDissolvedOxygenInPercentSaturation_2"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "5.57",
                                            "key": "waterPh_3"
                                        },
                                        {
                                            "value": "68.9",
                                            "key": "waterDissolvedOxygenInPercentSaturation_1"
                                        },
                                        {
                                            "value": "68",
                                            "key": "waterDissolvedOxygenInPercentSaturation_4"
                                        },
                                        {
                                            "value": 10,
                                            "key": "relativeWaterLevelDifferenceInCentimetres"
                                        },
                                        {
                                            "value": "5.55",
                                            "key": "waterPh_1"
                                        },
                                        {
                                            "value": "68",
                                            "key": "waterDissolvedOxygenInPercentSaturation_3"
                                        },
                                        {
                                            "value": "25.8",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_4"
                                        },
                                        {
                                            "value": "25.8",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_3"
                                        },
                                        {
                                            "value": "67.9",
                                            "key": "waterDissolvedOxygenInPercentSaturation_5"
                                        },
                                        {
                                            "value": "5.57",
                                            "key": "waterPh_4"
                                        },
                                        {
                                            "value": "25.8",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_2"
                                        },
                                        {
                                            "value": "5.57",
                                            "key": "waterPh_5"
                                        },
                                        {
                                            "value": "25.8",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_1"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "3",
                                            "key": "dipDurationInMinutes"
                                        },
                                        {
                                            "value": "6.81",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_4"
                                        },
                                        {
                                            "value": "6.8",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_5"
                                        },
                                        {
                                            "value": "6.86",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_2"
                                        },
                                        {
                                            "value": "6.81",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_3"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": 150.31964272901396,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": "41",
                                            "key": "piezometerHeightAboveGroundInCentimetres"
                                        },
                                        {
                                            "value": "6.91",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_1"
                                        },
                                        {
                                            "value": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.66397758593848,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": "2021-06-11T13:51:39+1000",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "909f6152-da08-4bf5-8a0d-abe223a2f0c4",
                        "dateCreated": "2021-06-11",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Piezometer Readings",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": "No Piezometer at exit stream",
                                            "key": "eventRemarks"
                                        },
                                        {
                                            "value": "13.7",
                                            "key": "waterTemperatureInDegreesCelcius_1"
                                        },
                                        {
                                            "value": "13.7",
                                            "key": "waterTemperatureInDegreesCelcius_3"
                                        },
                                        {
                                            "value": "13.7",
                                            "key": "waterTemperatureInDegreesCelcius_2"
                                        },
                                        {
                                            "value": "13.7",
                                            "key": "waterTemperatureInDegreesCelcius_5"
                                        },
                                        {
                                            "value": "13.7",
                                            "key": "waterTemperatureInDegreesCelcius_4"
                                        },
                                        {
                                            "value": "",
                                            "key": "piezometerId"
                                        },
                                        {
                                            "value": "0",
                                            "key": "totalWaterDepthInCentimetres"
                                        },
                                        {
                                            "value": "23.37",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_5"
                                        },
                                        {
                                            "value": "0",
                                            "key": "waterTableHeightInCentimetres"
                                        },
                                        {
                                            "value": "12:30 PM",
                                            "key": "eventTime"
                                        },
                                        {
                                            "value": "6.62",
                                            "key": "waterPh_2"
                                        },
                                        {
                                            "value": "92.6",
                                            "key": "waterDissolvedOxygenInPercentSaturation_2"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "6.62",
                                            "key": "waterPh_3"
                                        },
                                        {
                                            "value": "92.6",
                                            "key": "waterDissolvedOxygenInPercentSaturation_1"
                                        },
                                        {
                                            "value": "92.6",
                                            "key": "waterDissolvedOxygenInPercentSaturation_4"
                                        },
                                        {
                                            "value": 0,
                                            "key": "relativeWaterLevelDifferenceInCentimetres"
                                        },
                                        {
                                            "value": "6.63",
                                            "key": "waterPh_1"
                                        },
                                        {
                                            "value": "92.6",
                                            "key": "waterDissolvedOxygenInPercentSaturation_3"
                                        },
                                        {
                                            "value": "23.42",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_4"
                                        },
                                        {
                                            "value": "23.45",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_3"
                                        },
                                        {
                                            "value": "92.6",
                                            "key": "waterDissolvedOxygenInPercentSaturation_5"
                                        },
                                        {
                                            "value": "6.62",
                                            "key": "waterPh_4"
                                        },
                                        {
                                            "value": "23.41",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_2"
                                        },
                                        {
                                            "value": "6.62",
                                            "key": "waterPh_5"
                                        },
                                        {
                                            "value": "23.39",
                                            "key": "waterElectricalConductivityInMicrosiemensPerCentimetre_1"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "0",
                                            "key": "dipDurationInMinutes"
                                        },
                                        {
                                            "value": "9.61",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_4"
                                        },
                                        {
                                            "value": "9.61",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_5"
                                        },
                                        {
                                            "value": "9.61",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_2"
                                        },
                                        {
                                            "value": "9.61",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_3"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": 150.3196666343577,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": "0",
                                            "key": "piezometerHeightAboveGroundInCentimetres"
                                        },
                                        {
                                            "value": "9.61",
                                            "key": "waterDissolvedOxygenInMilligramsPerLitre_1"
                                        },
                                        {
                                            "value": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.662904270303585,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "54e93461-2ed1-4ab1-88e1-7d2bf42303d9",
                        "dateCreated": "2021-05-20",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Water Chemical Properties",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "Dr Ian Wright",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": "GCP1 270321",
                                            "key": "sampleId"
                                        },
                                        {
                                            "value": "2021-03-29T13:00:00Z",
                                            "key": "sampleAnalysisDate"
                                        },
                                        {
                                            "value": 150.31964272901396,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "measuredProperty": "Calcium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Potassium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Sodium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValue": "3.1",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Magnesium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Hardness (mgCaCo3/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValue": "3",
                                                    "measurementPql": "3"
                                                },
                                                {
                                                    "measuredProperty": "Hydroxide Alkalinity (OH-) (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Bicarbonate Alkalinity (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Carbonate Alkalinity (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Total Alkalinity as CaCo3 (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Sulphate (SO4) (mg/L)",
                                                    "measurementMethod": "Inorg-081",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Chloride (Cl) (mg/L)",
                                                    "measurementMethod": "Inorg-081",
                                                    "measuredValue": "3",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Ionic Balance (%)",
                                                    "measurementMethod": "Inorg-040",
                                                    "measuredValue": "4",
                                                    "measurementPql": "0"
                                                },
                                                {
                                                    "measuredProperty": "Arsenic - Total (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Boron - Total (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "20",
                                                    "measurementPql": "20"
                                                },
                                                {
                                                    "measuredProperty": "Barium (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "4",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Beryllium - Total (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Cobalt - Total (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Copper (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "12",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Aluminium (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "830",
                                                    "measurementPql": "10"
                                                },
                                                {
                                                    "measuredProperty": "Iron - Total (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "3600",
                                                    "measurementPql": "10"
                                                },
                                                {
                                                    "measuredProperty": "Manganese (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "11",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Lead (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Nickel (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Zinc (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "13",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Strontium (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "1.8",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Lithium (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Chromium (µg/L)",
                                                    "measurementMethod": "need relevant methods to be specified for this",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                }
                                            ],
                                            "key": "waterChemistryProperties"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.66397758593848,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": "2021-03-29T13:00:00Z",
                                            "key": "samplePreparationDate"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "8bc2f712-d694-43db-8af0-6520f1db29d4",
                        "dateCreated": "2021-06-09",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Water Chemical Properties",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "GCP1 March 2021",
                                            "key": "sampleId"
                                        },
                                        {
                                            "value": "2021-03-29T13:00:00Z",
                                            "key": "sampleAnalysisDate"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": "Data was collected and analysed by Dr Ian Wright of Western Sydney University. Data was input to BioCollect by Sarah Terkes.",
                                            "key": "eventRemarks"
                                        },
                                        {
                                            "value": "2021-03-29T13:00:00Z",
                                            "key": "samplePreparationDate"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": 150.31964272901396,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "measuredProperty": "Calcium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Potassium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Sodium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "3.1",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Magnesium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Hardness (mgCaCo3/L)",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "3",
                                                    "measurementPql": "3"
                                                },
                                                {
                                                    "measuredProperty": "Hydroxide Alkalinity (OH-) (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Bicarbonate Alkalinity (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Carbonate Alkalinity (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Total Alkalinity as CaCo3 (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Sulphate (SO4) (mg/L)",
                                                    "measurementMethod": "Inorg-081",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Chloride (Cl) (mg/L)",
                                                    "measurementMethod": "Inorg-081",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "3",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Ionic Balance (%)",
                                                    "measurementMethod": "Inorg-040",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "4",
                                                    "measurementPql": "0"
                                                },
                                                {
                                                    "measuredProperty": "Arsenic - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Boron - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "20",
                                                    "measurementPql": "20"
                                                },
                                                {
                                                    "measuredProperty": "Barium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "4",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Beryllium - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Cobalt - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Copper (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "12",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Aluminium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "830",
                                                    "measurementPql": "10"
                                                },
                                                {
                                                    "measuredProperty": "Iron - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "3600",
                                                    "measurementPql": "10"
                                                },
                                                {
                                                    "measuredProperty": "Manganese (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "11",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Lead (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Nickel (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Zinc (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "13",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Strontium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "1.8",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Lithium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Chromium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                }
                                            ],
                                            "key": "waterChemistryProperties"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.66397758593848,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "9b1e6edd-dacc-4e54-9afb-75e6ad0ce8ee",
                        "dateCreated": "2021-06-09",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Water Chemical Properties",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "GCP2 March 2021",
                                            "key": "sampleId"
                                        },
                                        {
                                            "value": "2021-03-29T13:00:00Z",
                                            "key": "sampleAnalysisDate"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": "Data was collected and analysed by Dr Ian Wright, and input into BioCollect by Sarah Terkes. There is no piezometer at this location - this is an exit stream.",
                                            "key": "eventRemarks"
                                        },
                                        {
                                            "value": "2021-03-29T13:00:00Z",
                                            "key": "samplePreparationDate"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": 150.3196666343577,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "measuredProperty": "Calcium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Potassium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Sodium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "3.1",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Magnesium (mg/L)",
                                                    "measurementMethod": "Metals-020",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Hardness (mgCaCo3/L)",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "3",
                                                    "measurementPql": "3"
                                                },
                                                {
                                                    "measuredProperty": "Hydroxide Alkalinity (OH-) (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Bicarbonate Alkalinity (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Carbonate Alkalinity (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Total Alkalinity as CaCo3 (mg/L)",
                                                    "measurementMethod": "Inorg-006",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Sulphate (SO4) (mg/L)",
                                                    "measurementMethod": "Inorg-081",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Chloride (Cl) (mg/L)",
                                                    "measurementMethod": "Inorg-081",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "3",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Ionic Balance (%)",
                                                    "measurementMethod": "Inorg-040",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "6",
                                                    "measurementPql": "0"
                                                },
                                                {
                                                    "measuredProperty": "Arsenic - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Boron - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "20",
                                                    "measurementPql": "20"
                                                },
                                                {
                                                    "measuredProperty": "Barium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "2",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Beryllium - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "0.5",
                                                    "measurementPql": "0.5"
                                                },
                                                {
                                                    "measuredProperty": "Cobalt - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Copper (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Aluminium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "220",
                                                    "measurementPql": "10"
                                                },
                                                {
                                                    "measuredProperty": "Iron - Total (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "180",
                                                    "measurementPql": "10"
                                                },
                                                {
                                                    "measuredProperty": "Manganese (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "5",
                                                    "measurementPql": "5"
                                                },
                                                {
                                                    "measuredProperty": "Lead (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Nickel (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Zinc (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "3",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Strontium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "=",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Lithium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                },
                                                {
                                                    "measuredProperty": "Chromium (µg/L)",
                                                    "measurementMethod": "Metals-022",
                                                    "measuredValueQualifier": "<",
                                                    "measuredValue": "1",
                                                    "measurementPql": "1"
                                                }
                                            ],
                                            "key": "waterChemistryProperties"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.662904270303585,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "78975aae-4d45-4269-9d90-d084f451888b",
                        "dateCreated": "2021-05-20",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Wetland Sediment Survey",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "Yes",
                                            "key": "contemporarySandLayerPresent"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "licence": "CC BY 3.0",
                                                    "identifier": "https://biocollect.ala.org.au/image?id=IMG_2557.JPG",
                                                    "notes": "",
                                                    "role": "surveyImage",
                                                    "filesize": 7974022,
                                                    "type": "image",
                                                    "activityId": "78975aae-4d45-4269-9d90-d084f451888b",
                                                    "outputId": "b2701293-aeda-4f74-9b65-58f189e937b4",
                                                    "filename": "processed_IMG_2557.JPG",
                                                    "filepath": "2021-05",
                                                    "attribution": "",
                                                    "name": "IMG_2557.JPG",
                                                    "documentId": "84951dda-d930-4e42-a7b8-5a49b5909e9e",
                                                    "contentType": "image/jpeg",
                                                    "dateTaken": "2021-03-26T23:48:15Z",
                                                    "formattedSize": "7.97 MB",
                                                    "status": "active"
                                                }
                                            ],
                                            "key": "corePhoto"
                                        },
                                        {
                                            "value": "20",
                                            "key": "clayStackDepthInCentimetres"
                                        },
                                        {
                                            "value": [],
                                            "key": "clayStackPhoto"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": [],
                                            "key": "sedimentSubSampleRepeatSection"
                                        },
                                        {
                                            "value": "13",
                                            "key": "peatStackDepthInCentimetres"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": [],
                                            "key": "peatStackPhoto"
                                        },
                                        {
                                            "value": 150.31964272901396,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.66397758593848,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": "GCP1 270321",
                                            "key": "coreId"
                                        },
                                        {
                                            "value": "0",
                                            "key": "alternatingOrganicSandLayerThicknessInCentimetres"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "930c54f8-4dbf-4169-a417-c129c054dbf8",
                        "dateCreated": "2021-06-09",
                        "description": null,
                        "outputs": [
                            {
                                "name": "BMWHI - Wetland Sediment Survey",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": null,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "No",
                                            "key": "contemporarySandLayerPresent"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "licence": "CC BY 3.0",
                                                    "identifier": "https://biocollect.ala.org.au/image?id=IMG_2557_%281%29.JPG",
                                                    "notes": "",
                                                    "role": "surveyImage",
                                                    "filesize": 7974022,
                                                    "type": "image",
                                                    "activityId": "930c54f8-4dbf-4169-a417-c129c054dbf8",
                                                    "outputId": "a2e062e2-cbeb-4e59-be31-618f9f2c4e49",
                                                    "filename": "processed_IMG_2557_(1).JPG",
                                                    "filepath": "2021-06",
                                                    "attribution": "",
                                                    "name": "IMG_2557_(1).JPG",
                                                    "documentId": "1501d72d-c008-4253-9af2-c1ef140be6e4",
                                                    "contentType": "image/jpeg",
                                                    "dateTaken": "2021-03-26T23:48:15Z",
                                                    "formattedSize": "7.97 MB",
                                                    "status": "active"
                                                }
                                            ],
                                            "key": "corePhoto"
                                        },
                                        {
                                            "value": "20",
                                            "key": "clayStackDepthInCentimetres"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": [],
                                            "key": "sedimentSubSampleRepeatSection"
                                        },
                                        {
                                            "value": "13",
                                            "key": "peatStackDepthInCentimetres"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": 150.31964272901396,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.66397758593848,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": "GCP1 MARCH 2021",
                                            "key": "coreId"
                                        },
                                        {
                                            "value": "0",
                                            "key": "alternatingOrganicSandLayerThicknessInCentimetres"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "eventDate"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "activityId": "453821ed-74ff-421f-b031-e4fa35685367",
                        "dateCreated": "2021-06-09",
                        "description": null,
                        "outputs": [
                            {
                                "name": "Bush After Fire",
                                "data": {
                                    "dataList": [
                                        {
                                            "value": "No",
                                            "key": "recentFireHistoryBoolean"
                                        },
                                        {
                                            "value": "Please note this is a dummy data recording - do not include in final results analysis",
                                            "key": "locationDescription"
                                        },
                                        {
                                            "value": "North",
                                            "key": "locationPhotoDirection"
                                        },
                                        {
                                            "value": "No",
                                            "key": "contactAgreement"
                                        },
                                        {
                                            "value": "2021-03-26T13:00:00Z",
                                            "key": "observationDate"
                                        },
                                        {
                                            "value": {
                                                "listId": "",
                                                "commonName": null,
                                                "outputSpeciesId": "494cb998-db3a-4575-ba1c-87cb8aff7e12",
                                                "scientificName": "Eucalyptus",
                                                "name": "Eucalyptus",
                                                "guid": "https://id.biodiversity.org.au/taxon/apni/51302291"
                                            },
                                            "key": "treeSpecies"
                                        },
                                        {
                                            "value": "Native vegetation",
                                            "key": "landuse"
                                        },
                                        {
                                            "value": "0",
                                            "key": "scorchHeightAboveGroundInMetres"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLongitude"
                                        },
                                        {
                                            "value": [],
                                            "key": "simplePhotoProtocolCanopy"
                                        },
                                        {
                                            "value": 50,
                                            "key": "locationAccuracy"
                                        },
                                        {
                                            "value": "Unburnt",
                                            "key": "severityClass"
                                        },
                                        {
                                            "value": [],
                                            "key": "simplePhotoProtocolSky"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "vegetationLayerShrubs": "0",
                                                    "vegetationLayerSubCanopy": "0",
                                                    "vegetationLayerGround": "0",
                                                    "percentOfFireImpactClass": "Height of layer (m)",
                                                    "vegetationLayerTrees": "0"
                                                },
                                                {
                                                    "vegetationLayerShrubs": "0",
                                                    "vegetationLayerSubCanopy": "0",
                                                    "vegetationLayerGround": "0",
                                                    "percentOfFireImpactClass": "% Cover of living vegetation",
                                                    "vegetationLayerTrees": "0"
                                                },
                                                {
                                                    "vegetationLayerShrubs": "0",
                                                    "vegetationLayerSubCanopy": "0",
                                                    "vegetationLayerGround": "0",
                                                    "percentOfFireImpactClass": "% Cover of vegetation scorched (brown) but not fully consumed by fire",
                                                    "vegetationLayerTrees": "0"
                                                },
                                                {
                                                    "vegetationLayerShrubs": "0",
                                                    "vegetationLayerSubCanopy": "0",
                                                    "vegetationLayerGround": "0",
                                                    "percentOfFireImpactClass": "% Cover of vegetation that would have been fully consumed by fire",
                                                    "vegetationLayerTrees": "0"
                                                }
                                            ],
                                            "key": "vegetationStructuretable"
                                        },
                                        {
                                            "value": "Dry Sclerophyll",
                                            "key": "vegetationStructuralType"
                                        },
                                        {
                                            "value": "Ridge",
                                            "key": "topography"
                                        },
                                        {
                                            "value": null,
                                            "key": "locationLatitude"
                                        },
                                        {
                                            "value": [
                                                {
                                                    "licence": "CC BY 3.0",
                                                    "identifier": "https://biocollect.ala.org.au/image?id=165112210_2854505828209118_8324485622534677359_n.jpg",
                                                    "notes": "",
                                                    "role": "surveyImage",
                                                    "filesize": 533833,
                                                    "type": "image",
                                                    "activityId": "453821ed-74ff-421f-b031-e4fa35685367",
                                                    "outputId": "1601aa91-2e38-4080-a519-da18ead87143",
                                                    "filename": "165112210_2854505828209118_8324485622534677359_n.jpg",
                                                    "filepath": "2021-06",
                                                    "attribution": "",
                                                    "name": "165112210_2854505828209118_8324485622534677359_n.jpg",
                                                    "documentId": "da9c2f59-35d6-42a9-b03f-c8f07c5f2afb",
                                                    "contentType": "image/jpeg",
                                                    "dateTaken": "2021-06-09T04:15:08Z",
                                                    "formattedSize": "533.83 KB",
                                                    "status": "active"
                                                }
                                            ],
                                            "key": "locationPhoto"
                                        },
                                        {
                                            "value": [],
                                            "key": "simplePhotoProtocolSouth"
                                        },
                                        {
                                            "value": "Sarah Terkes",
                                            "key": "recordedBy"
                                        },
                                        {
                                            "value": "Low Cover <30%",
                                            "key": "foliageProjectedCoverEstimateCategorical"
                                        },
                                        {
                                            "value": 150.3196666343577,
                                            "key": "locationCentroidLongitude"
                                        },
                                        {
                                            "value": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
                                            "key": "location"
                                        },
                                        {
                                            "value": -33.662904270303585,
                                            "key": "locationCentroidLatitude"
                                        },
                                        {
                                            "value": [],
                                            "key": "simplePhotoProtocolNorth"
                                        },
                                        {
                                            "value": [],
                                            "key": "simplePhotoProtocolGround"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
}''')

macro_invertebrate_survey = json.loads('''{
	"data": {
		"searchBioCollectProject": [{
			"projectId": "f72f7cbc-5ccd-480f-8a4c-0a9a3a5c9cae",
			"name": "Blue Mountains Upland Swamps",
			"sites": [{
					"siteId": "747ac352-6ad7-438e-905a-e7a8bc2533dc",
					"name": "Project area for Blue Mountains Upland Swamps",
					"externalSiteId": null,
					"type": "",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.13366699218747, -33.50269783481254], [150.6719970703125, -33.628570663568816], [150.64727783203125, -33.91396172610034], [150.15014648437497, -33.761110320624105], [150.13366699218747, -33.50269783481254]]"
							]
						}
					}
				},
				{
					"siteId": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
					"name": "Grand Canyon Swamp Exit Stream",
					"externalSiteId": null,
					"type": "monitoringPoint",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.32015562057492, -33.66076032976858], [150.32097101211548, -33.660867489391755], [150.3197479248047, -33.66511804679502], [150.31882524490354, -33.66501089246613], [150.3186535835266, -33.66251058690082], [150.32015562057492, -33.66076032976858]]"
							]
						}
					}
				},
				{
					"siteId": "89030c0b-d965-428c-8bf0-ab165e74bf2e",
					"name": "Private site for survey: Water table monitoring - piezometer recordings",
					"externalSiteId": null,
					"type": null,
					"catchment": null,
					"status": "active",
					"visibility": "private",
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.20166166126725, -33.741213210385865], [150.20264871418476, -33.738679434257975], [150.204494073987, -33.7364310913657], [150.20900018513203, -33.73707348106183], [150.20698316395283, -33.738500996498566], [150.20535238087177, -33.7408563450369], [150.20591028034687, -33.74249791334891], [150.2029062062502, -33.74264065693483], [150.2015758305788, -33.74246222741532], [150.20166166126725, -33.741213210385865]]"
							]
						}
					}
				},
				{
					"siteId": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
					"name": "Grand Canyon Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.32114267349243, -33.664417969351916], [150.3196406364441, -33.665400219140835], [150.3185784816742, -33.66493588427473], [150.31943678855896, -33.66214982244585], [150.32015562057492, -33.662194471583966], [150.31997323036194, -33.66400720702358], [150.32114267349243, -33.664417969351916]]"
							]
						}
					}
				},
				{
					"siteId": "a2f70dd0-cbf6-4385-876d-d929baed584f",
					"name": "Lawson Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.42689681053162, -33.7149678272743], [150.4276478290558, -33.71527125443331], [150.42726159095764, -33.71724350482991], [150.42623162269592, -33.71696685705355], [150.42689681053162, -33.7149678272743]]"
							]
						}
					}
				},
				{
					"siteId": "23caa0cb-30c9-419b-9963-7056ec614fe5",
					"name": "Lawson Swamp Culvert Exit Stream",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.42691826820374, -33.7149856759604], [150.42765855789185, -33.71524448149183], [150.42720794677734, -33.71733274585793], [150.4262101650238, -33.717207808392715], [150.4265856742859, -33.71592272676971], [150.42691826820374, -33.7149856759604]]"
							]
						}
					}
				},
				{
					"siteId": "4f494553-ec14-4197-837f-d5f502c21ed9",
					"name": "Bullaburra Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.41271328926086, -33.727038046362914], [150.41303515434265, -33.727154046444525], [150.4132229089737, -33.727814351615024], [150.4129761457443, -33.72790804315332], [150.41260600090027, -33.727336969331596], [150.41268646717072, -33.727038046362914], [150.41271328926086, -33.727020200182594], [150.41271328926086, -33.727038046362914]]"
							]
						}
					}
				},
				{
					"siteId": "e1460811-ad65-445e-a933-84fdb25728c3",
					"name": "Bullaburra Swamp Exit Stream",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.41265964508057, -33.7270603540831], [150.4129707813263, -33.727100507964806], [150.41321218013763, -33.727814351615024], [150.41296005249023, -33.72792142765044], [150.41258990764618, -33.72718081567187], [150.41265964508057, -33.7270603540831]]"
							]
						}
					}
				}
			],
			"surveys": [{
				"surveyDetails": {
					"surveyMetadata": {
						"name": "Macro-invertebrate Survey",
						"description": "Sampling of macro-invertebrate populations as an indicator of wetland health.",
						"version": 6,
						"methodType": "systematic",
						"methodName": "Water quality - Macroinvertebrate survey - SIGNAL2 method",
						"startDate": "2021-03-27",
						"endDate": null,
						"pActivityFormName": "ACT Waterwatch - Water Bug Survey",
						"dataSharingLicense": "https://creativecommons.org/licenses/by/4.0/",
						"legalCustodianOrganisation": "Blue Mountains World Heritage Institute",
						"spatialAccuracy": "high",
						"temporalAccuracy": "high",
						"speciesIdentification": "moderate",
						"nonTaxonomicAccuracy": "high",
						"dataQualityAssuranceMethods": [
							"dataownercurated",
							"systemsupported"
						],
						"dataQualityAssuranceDescription": "",
						"dataManagementPolicyDocument": "",
						"status": "active",
						"dataAccessExternalURL": "",
						"isDataManagementPolicyDocumented": false,
						"sites": [
							"e1460811-ad65-445e-a933-84fdb25728c3",
							"4f494553-ec14-4197-837f-d5f502c21ed9",
							"e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
							"b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
							"23caa0cb-30c9-419b-9963-7056ec614fe5",
							"a2f70dd0-cbf6-4385-876d-d929baed584f"
						]
					},
					"surveyForms": [{
						"name": "ACT Waterwatch - Water Bug Survey",
						"version": 36,
						"activationDate": null,
						"publicationStatus": "published",
						"type": "Assessment",
						"status": "active",
						"formSections": [{
							"title": null,
							"name": "ACT Waterwatch - Water Bug Survey",
							"templateName": "actWaterwatch-waterBugSurvey",
							"formTemplate": {
								"sectionTemplate": {
									"excludeAbsenceRecord": "true",
									"modelName": "ACT_Waterwatch_Modified_SIGNAL2_macroinvertebrates",
									"record": "true",
									"dataModel": [{
											"indexName": "taxaRichness",
											"dataType": "number",
											"name": "taxaRichness",
											"description": "Taxa richness"
										},
										{
											"dataType": "number",
											"name": "spiValue",
											"description": "Calculated stream pollution index (SPI)"
										},
										{
											"indexName": "overallSiteQuality",
											"dataType": "text",
											"name": "streamQualityRating",
											"description": "Stream quality rating"
										},
										{
											"dataType": "text",
											"name": "samplingProtocol",
											"dwcAttribute": "samplingProtocol",
											"value": "SIGNAL2 aquatic macroinvertebrates"
										},
										{
											"indexName": "surveyDate",
											"dataType": "date",
											"name": "surveyDate",
											"dwcAttribute": "surveyDate",
											"description": "The date on which the survey was undertaken",
											"validate": "required,past[now]"
										},
										{
											"dataType": "time",
											"name": "surveyTime",
											"dwcAttribute": "eventTime",
											"description": "The time of the day that the survey was undertaken",
											"validate": "required"
										},
										{
											"dataType": "number",
											"name": "surveyDuration",
											"description": "The duration of the sampling event in decimal hours"
										},
										{
											"dataType": "text",
											"name": "eventRemarks",
											"dwcAttribute": "eventRemarks",
											"description": "General remarks about the survey event, including any characteristic site features, conditions such as cloudy, sunny or raining, whether the sampling was done in a shady place or in the open, etc."
										},
										{
											"indexName": "recordedBy",
											"dataType": "text",
											"name": "recordedBy",
											"dwcAttribute": "recordedBy",
											"noEdit": "true",
											"description": "The name of the person or group undertaking the sampling event.",
											"validate": "required"
										},
										{
											"indexName": "samplingMethod",
											"dataType": "stringList",
											"name": "samplingMethod",
											"description": "The method used to sample the waterbody for macroinvertebrates.",
											"constraints": [
												"Kick",
												"Sweep"
											],
											"validate": "required"
										},
										{
											"disableTableUpload": true,
											"columns": [{
													"indexName": "habitatType",
													"dataType": "text",
													"name": "habitatType",
													"description": "Select the type of habitat sampled",
													"constraints": [
														"Silt and sand",
														"Stones",
														"Water plants",
														"Leaves and twigs",
														"Logs branches and tree roots"
													]
												},
												{
													"dataType": "boolean",
													"name": "edge"
												},
												{
													"dataType": "boolean",
													"name": "pool"
												},
												{
													"dataType": "boolean",
													"name": "riffle"
												}
											],
											"dataType": "list",
											"name": "habitatSampled"
										},
										{
											"dataType": "text",
											"name": "idConfirmedBy",
											"description": "Verification of this record by a qualified person will help to make it more useful in scientific analysis of the data.",
											"constraints": [
												"Waterwatch coordinator",
												"Professional staff of council or agency",
												"Experienced teacher",
												"Community member",
												"Other (specify in notes)"
											]
										},
										{
											"indexName": "gambusiaPresent",
											"dataType": "text",
											"name": "gambusiaPresent",
											"description": "Gambusia is an introduced freshwater pest species which damages the aquatic environment.",
											"constraints": [
												"Yes",
												"No"
											]
										},
										{
											"dataType": "text",
											"name": "wqFactors",
											"description": "Please note any factors apparent during your sampling which may affect water quality. (eg. muddy or very clear water, the amount of algae present, etc.."
										},
										{
											"dataType": "text",
											"name": "observationRemarks",
											"dwcAttribute": "observationRemarks",
											"description": "Observation notes about the record."
										},
										{
											"defaultAccuracy": 50,
											"hideMyLocation": true,
											"columns": [{
													"dwcAttribute": "verbatimLatitude",
													"source": "locationLatitude"
												},
												{
													"dwcAttribute": "verbatimLongitude",
													"source": "locationLongitude"
												},
												{
													"source": "Locality"
												},
												{
													"source": "Accuracy"
												},
												{
													"source": "Notes"
												},
												{
													"source": "Source"
												}
											],
											"dataType": "geoMap",
											"name": "location",
											"hideSiteSelection": false,
											"zoomToProjectArea": true,
											"validate": "required"
										},
										{
											"readonly": true,
											"indexName": "siteName",
											"dataType": "text",
											"name": "siteName",
											"noEdit": true
										},
										{
											"allowRowDelete": false,
											"disableTableUpload": true,
											"columns": [{
													"dataType": "species",
													"name": "taxonName"
												},
												{
													"dataType": "text",
													"name": "taxonSensitivityClass",
													"description": "Different macroinvertebrate species/taxa have different degrees of sensitivity to water quality conditions and can be an indicator of changes. Grouping them into broad categories makes it easier to relate the species that you see with the calculated water quality."
												},
												{
													"dataType": "number",
													"name": "taxonSensitivityRating",
													"description": "A rating between 1 and 10 which reflects the relative sensitivity of different species/taxa of macroinvertebrates to water quality factors."
												},
												{
													"dataType": "number",
													"name": "individualCount",
													"dwcAttribute": "individualCount",
													"description": "Enter the actual number of each species/taxon that you count in your sample.",
													"validate": "integer,min[0]"
												},
												{
													"dataType": "number",
													"name": "taxonWeightFactor"
												},
												{
													"dataType": "number",
													"name": "taxonIndexValue"
												}
											],
											"dataType": "list",
											"name": "taxaObservations",
											"jsMain": "https://dl.dropbox.com/s/qdv5zznw7grsuy1/taxaObservations.js?dl=0",
											"defaultRows": [{
													"scientificName": "Mecoptera",
													"taxonSensitivityClass": "Very Sensitive",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Scorpion flies",
														"scientificName": "Mecoptera",
														"name": "Scorpion flies (Mecoptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:67c46151-7449-407a-a8b3-a283ba3f0771"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "10"
												},
												{
													"scientificName": "Plecoptera",
													"taxonSensitivityClass": "Very Sensitive",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Stone flies",
														"scientificName": "Plecoptera",
														"name": "Stone flies (Plecoptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:4fbe14c4-2efb-4874-8842-f29e05a93f92"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "10"
												},
												{
													"scientificName": "Ephemeroptera",
													"taxonSensitivityClass": "Very Sensitive",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "May flies",
														"scientificName": "Ephemeroptera",
														"name": "May flies (Ephemeroptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:928c5312-17a2-4557-b523-d207cacc332b"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "9"
												},
												{
													"scientificName": "Megaloptera",
													"taxonSensitivityClass": "Very Sensitive",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Alder flies",
														"scientificName": "Megaloptera",
														"name": "Alder flies (Megaloptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:1764aba8-641d-4eb8-ade5-ff33efafb054"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "8"
												},
												{
													"scientificName": "Trichoptera",
													"taxonSensitivityClass": "Very Sensitive",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Caddis flies",
														"scientificName": "Trichoptera",
														"name": "Caddis flies (Trichoptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:0964bf51-f620-4a71-9ab3-ff631f2099bb"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "8"
												},
												{
													"scientificName": "Nematomorpha",
													"taxonSensitivityClass": "Sensitive",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Horsehair worms; gordian worms",
														"scientificName": "Nematomorpha",
														"name": "Horsehair worms; gordian worms (Nematomorpha)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:4b1dd080-6a02-48c4-9f6c-94680f7651dd"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "6"
												},
												{
													"scientificName": "Acari",
													"taxonSensitivityClass": "Sensitive",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Mites",
														"scientificName": "Acarina",
														"name": "Mites (Acarina)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:c731c9bb-6292-4071-873d-2e8543dd120f"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "6"
												},
												{
													"scientificName": "Anaspidacea",
													"taxonSensitivityClass": "Sensitive",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Cave shrimp",
														"scientificName": "Anaspidacea",
														"name": "Cave shrimp (Anaspidacea)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:5b4de720-d042-47b3-824a-542b12e7c771"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "6"
												},
												{
													"scientificName": "Neuroptera",
													"taxonSensitivityClass": "Sensitive",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Lacewings",
														"scientificName": "Neuroptera",
														"name": "Lacewings (Neuroptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:db09c273-56ae-4ef9-a5ed-53027aa7c63e"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "6"
												},
												{
													"scientificName": "Coleoptera",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Beetles - Riffle beetles, Whirligigs",
														"scientificName": "Coleoptera",
														"name": "Beetles - Riffle beetles, Whirligigs (Coleoptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:5c387616-0cb4-42f0-936e-7ec22d576939"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "5"
												},
												{
													"scientificName": "Porifera",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Freshwater sponges",
														"scientificName": "Porifera",
														"name": "Freshwater sponges (Porifera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:ed334702-b153-41b0-ac93-e6aa4964331c"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "4"
												},
												{
													"scientificName": "Bryozoa",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Pipe-mosses",
														"scientificName": "Bryozoa",
														"name": "Pipe-mosses (Bryozoa)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:a1f069f9-eaa8-487c-889a-d3cfb3dd936e"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "4"
												},
												{
													"scientificName": "Decapoda",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Yabbies; crayfish, shrimp",
														"scientificName": "Decapoda",
														"name": "Yabbies; crayfish, shrimp (Decapoda)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:2f12112b-d593-4392-a9db-4b026b8805a3"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "4"
												},
												{
													"scientificName": "Diplopoda",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Aquatic millipedes",
														"scientificName": "Diplopoda",
														"name": "Aquatic millipedes (Diplopoda)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:0a08c6cb-7990-4124-ac83-9d44274d6a84"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "4"
												},
												{
													"scientificName": "Nemertea",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Proboscis worms",
														"scientificName": "Nemertea",
														"name": "Proboscis worms (Nemertea)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:89e92ab7-7ffc-4cc4-9149-19c8f8079940"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "3"
												},
												{
													"scientificName": "Nematoda",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Nematodes, roundworms",
														"scientificName": "Nematoda",
														"name": "Nematodes, roundworms (Nematoda)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:0e7e0f7d-4456-495b-b762-2d11f78b9368"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "3"
												},
												{
													"scientificName": "Bivalvia",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Freshwater mussels; clams",
														"scientificName": "Bivalvia",
														"name": "Freshwater mussels; clams (Bivalvia)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:8c3070f6-9475-4b6a-95cb-8afb944ad3d5"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "3"
												},
												{
													"scientificName": "Amphipoda",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Side-swimmers; scuds",
														"scientificName": "Amphipoda",
														"name": "Side-swimmers; scuds (Amphipoda)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:c799e373-f43a-446d-b2d0-836e6be97b84"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "3"
												},
												{
													"scientificName": "Diptera",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Fly larva - mosquito larvae, bloodworms",
														"scientificName": "Diptera",
														"name": "Fly larva - mosquito larvae, bloodworms (Diptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:933b2bf6-deee-4fd9-b669-4bf8cf7cc9ce"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "3"
												},
												{
													"scientificName": "Odonata",
													"taxonSensitivityClass": "Moderately Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Dragonfly; damselflies",
														"scientificName": "Odonata",
														"name": "Dragonfly; damselflies (Odonata)",
														"guid": "NZOR-4-24409"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "3"
												},
												{
													"scientificName": "Turbellaria",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Flatworms",
														"scientificName": "Turbellaria",
														"name": "Flatworms (Turbellaria)",
														"guid": "13010000"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "2"
												},
												{
													"scientificName": "Oligochaeta",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Segmented worms",
														"scientificName": "Oligochaeta",
														"name": "Segmented worms (Oligochaeta)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:406916d5-9058-4d72-9dbf-d3f689e8f3b2"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "2"
												},
												{
													"scientificName": "Isopoda",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Freshwater Slaters",
														"scientificName": "Isopoda",
														"name": "Freshwater Slaters (Isopoda)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:e4720a22-d642-44c7-abc6-fb5b34d5e057"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "2"
												},
												{
													"scientificName": "Hemiptera",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "True bugs - backswimmers, water boatman, needle bugs",
														"scientificName": "Hemiptera",
														"name": "True bugs - backswimmers, water boatman, needle bugs (Hemiptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:7630fe33-a00e-4743-80da-4fa6a36cd8b2"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "6"
												},
												{
													"scientificName": "Lepidoptera",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Moth larvae",
														"scientificName": "Lepidoptera",
														"name": "Moth larvae (Lepidoptera)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:7cb6c81c-a7c4-4dd5-8578-fcfd2de847d6"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "3"
												},
												{
													"scientificName": "Hydrozoa",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Hydras",
														"scientificName": "Hydrozoa",
														"name": "Hydras (Hydrozoa)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:40e34a43-accb-48e3-9492-09c39ac5f756"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												},
												{
													"scientificName": "Gastropoda",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Freshwater Snails",
														"scientificName": "Gastropoda",
														"name": "Freshwater Snails (Gastropoda)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:ab81c7fc-3fc3-4e54-b277-a12a1a9cd0d8"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												},
												{
													"scientificName": "Hirudinea",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Leechs",
														"scientificName": "Hirudinea",
														"name": "Leechs (Hirudinea)",
														"guid": "22300000"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												},
												{
													"scientificName": "Polychaeta",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Bristleworms",
														"scientificName": "Polychaeta",
														"name": "Bristleworms (Polychaeta)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:d1251470-e6f7-4f43-b97d-276dab41b06b"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												},
												{
													"scientificName": "Anostraca",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Brine shrimps; fairy shrimps",
														"scientificName": "Anostraca",
														"name": "Brine shrimps; fairy shrimps (Anostraca)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:dbc4f4ad-0ad5-4813-9275-95b00b448832"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												},
												{
													"scientificName": "Branchiura",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Fish lice",
														"scientificName": "Branchiura",
														"name": "Fish lice (Branchiura)",
														"guid": "NZOR-4-111042"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												},
												{
													"scientificName": "Cyclestheriidae",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Clam shrimps",
														"scientificName": "Cyclestheriidae",
														"name": "Clam shrimps (Cyclestheriidae)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:925a4c2a-19fe-43c9-af4c-9b420b85b13a"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												},
												{
													"scientificName": "Notostraca",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Tadpole shrimp",
														"scientificName": "Notostraca",
														"name": "Tadpole shrimp (Notostraca)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:7d0c7db7-6e86-4c63-bb4c-ca80c1b84a06"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												},
												{
													"scientificName": "Collembola",
													"taxonSensitivityClass": "Very Tolerant",
													"taxonIndexValue": "",
													"dataType": "species",
													"taxonWeightFactor": "",
													"individualCount": "",
													"taxonName": {
														"commonName": "Springtails",
														"scientificName": "Collembola",
														"name": "Springtails (Collembola)",
														"guid": "urn:lsid:biodiversity.org.au:afd.taxon:53e5e456-0d08-4cff-ac1f-d453b2c07e3b"
													},
													"dwcAttribute": "scientificName",
													"taxonSensitivityRating": "1"
												}
											]
										}
									]
								}
							}
						}]
					}]
				}
			}]
		}]
	}
}''')

surface_water_mineral_composition_survey = json.loads('''{
	"data": {
		"searchBioCollectProject": [{
			"projectId": "f72f7cbc-5ccd-480f-8a4c-0a9a3a5c9cae",
			"name": "Blue Mountains Upland Swamps",
			"sites": [{
					"siteId": "747ac352-6ad7-438e-905a-e7a8bc2533dc",
					"name": "Project area for Blue Mountains Upland Swamps",
					"externalSiteId": null,
					"type": "",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.13366699218747, -33.50269783481254], [150.6719970703125, -33.628570663568816], [150.64727783203125, -33.91396172610034], [150.15014648437497, -33.761110320624105], [150.13366699218747, -33.50269783481254]]"
							]
						}
					}
				},
				{
					"siteId": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
					"name": "Grand Canyon Swamp Exit Stream",
					"externalSiteId": null,
					"type": "monitoringPoint",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.32015562057492, -33.66076032976858], [150.32097101211548, -33.660867489391755], [150.3197479248047, -33.66511804679502], [150.31882524490354, -33.66501089246613], [150.3186535835266, -33.66251058690082], [150.32015562057492, -33.66076032976858]]"
							]
						}
					}
				},
				{
					"siteId": "89030c0b-d965-428c-8bf0-ab165e74bf2e",
					"name": "Private site for survey: Water table monitoring - piezometer recordings",
					"externalSiteId": null,
					"type": null,
					"catchment": null,
					"status": "active",
					"visibility": "private",
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.20166166126725, -33.741213210385865], [150.20264871418476, -33.738679434257975], [150.204494073987, -33.7364310913657], [150.20900018513203, -33.73707348106183], [150.20698316395283, -33.738500996498566], [150.20535238087177, -33.7408563450369], [150.20591028034687, -33.74249791334891], [150.2029062062502, -33.74264065693483], [150.2015758305788, -33.74246222741532], [150.20166166126725, -33.741213210385865]]"
							]
						}
					}
				},
				{
					"siteId": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
					"name": "Grand Canyon Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.32114267349243, -33.664417969351916], [150.3196406364441, -33.665400219140835], [150.3185784816742, -33.66493588427473], [150.31943678855896, -33.66214982244585], [150.32015562057492, -33.662194471583966], [150.31997323036194, -33.66400720702358], [150.32114267349243, -33.664417969351916]]"
							]
						}
					}
				},
				{
					"siteId": "a2f70dd0-cbf6-4385-876d-d929baed584f",
					"name": "Lawson Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.42689681053162, -33.7149678272743], [150.4276478290558, -33.71527125443331], [150.42726159095764, -33.71724350482991], [150.42623162269592, -33.71696685705355], [150.42689681053162, -33.7149678272743]]"
							]
						}
					}
				},
				{
					"siteId": "23caa0cb-30c9-419b-9963-7056ec614fe5",
					"name": "Lawson Swamp Culvert Exit Stream",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.42691826820374, -33.7149856759604], [150.42765855789185, -33.71524448149183], [150.42720794677734, -33.71733274585793], [150.4262101650238, -33.717207808392715], [150.4265856742859, -33.71592272676971], [150.42691826820374, -33.7149856759604]]"
							]
						}
					}
				},
				{
					"siteId": "4f494553-ec14-4197-837f-d5f502c21ed9",
					"name": "Bullaburra Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.41271328926086, -33.727038046362914], [150.41303515434265, -33.727154046444525], [150.4132229089737, -33.727814351615024], [150.4129761457443, -33.72790804315332], [150.41260600090027, -33.727336969331596], [150.41268646717072, -33.727038046362914], [150.41271328926086, -33.727020200182594], [150.41271328926086, -33.727038046362914]]"
							]
						}
					}
				},
				{
					"siteId": "e1460811-ad65-445e-a933-84fdb25728c3",
					"name": "Bullaburra Swamp Exit Stream",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.41265964508057, -33.7270603540831], [150.4129707813263, -33.727100507964806], [150.41321218013763, -33.727814351615024], [150.41296005249023, -33.72792142765044], [150.41258990764618, -33.72718081567187], [150.41265964508057, -33.7270603540831]]"
							]
						}
					}
				}
			],
			"surveys": [{
				"surveyDetails": {
					"surveyMetadata": {
						"name": "Surface Water Mineral Composition",
						"description": "This survey is systematically collecting and analysing surface water samples for chemical and mineral composition and to monitor changes in these parameters over time. Correlations between these data and data from other surveys will reveal relationships and dependencies between different parameters in respect to ecosystem function.",
						"version": 9,
						"methodType": "systematic",
						"methodName": "Water quality - Standardised physical/chemical attribute measurements",
						"startDate": "2021-03-27",
						"endDate": null,
						"pActivityFormName": "BMWHI - Water Chemical Properties",
						"dataSharingLicense": "https://creativecommons.org/licenses/by/4.0/",
						"legalCustodianOrganisation": "Blue Mountains World Heritage Institute",
						"spatialAccuracy": "high",
						"temporalAccuracy": "high",
						"speciesIdentification": "na",
						"nonTaxonomicAccuracy": "high",
						"dataQualityAssuranceMethods": [
							"dataownercurated",
							"systemsupported"
						],
						"dataQualityAssuranceDescription": "",
						"dataManagementPolicyDocument": "",
						"status": "active",
						"dataAccessExternalURL": "",
						"isDataManagementPolicyDocumented": false,
						"sites": [
							"e1460811-ad65-445e-a933-84fdb25728c3",
							"4f494553-ec14-4197-837f-d5f502c21ed9",
							"e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
							"b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
							"23caa0cb-30c9-419b-9963-7056ec614fe5",
							"a2f70dd0-cbf6-4385-876d-d929baed584f"
						]
					},
					"surveyForms": [{
						"name": "BMWHI - Water Chemical Properties",
						"version": 21,
						"activationDate": null,
						"publicationStatus": "published",
						"type": "Assessment",
						"status": "active",
						"formSections": [{
							"title": null,
							"name": "BMWHI - Water Chemical Properties",
							"templateName": "bmwhiWaterChemicalProperties",
							"formTemplate": {
								"sectionTemplate": {
									"modelName": "BMWHI - Water Chemical Properties",
									"dataModel": [{
											"dataType": "text",
											"description": "The name of the person who made the observation (edit the default name if appropriate).",
											"name": "recordedBy",
											"dwcAttribute": "recordedBy",
											"validate": "required"
										},
										{
											"dataType": "date",
											"description": "The date that the sample was collected in the field.",
											"name": "eventDate",
											"dwcAttribute": "eventDate",
											"defaultValue": "${now}",
											"validate": "required"
										},
										{
											"dataType": "text",
											"description": "A unique identifier for the collected sample. [This will generally match the label on the sample bottle].",
											"name": "sampleId",
											"validate": "required"
										},
										{
											"dataType": "date",
											"description": "The date that the sample was prepared for analysis.",
											"name": "samplePreparationDate"
										},
										{
											"dataType": "date",
											"description": "The date that the sample was analysed.",
											"name": "sampleAnalysisDate"
										},
										{
											"dataType": "text",
											"name": "eventRemarks",
											"description": "General observational notes applicable to the site, conditions, sampling undertaken, etc.",
											"dwcAttribute": "eventRemarks"
										},
										{
											"columns": [{
													"dwcAttribute": "verbatimLatitude",
													"source": "locationLatitude"
												},
												{
													"dwcAttribute": "verbatimLongitude",
													"source": "locationLongitude"
												},
												{
													"source": "Locality"
												},
												{
													"description": "",
													"source": "Accuracy"
												},
												{
													"description": "Describe the location. E.g. approximately 200m south of currency creek settlement at Lions Park walking trail entrance",
													"source": "Notes"
												},
												{
													"source": "Source"
												}
											],
											"dataType": "geoMap",
											"name": "location",
											"validate": "required"
										},
										{
											"dataType": "text",
											"name": "sampleId",
											"description": "Unique identifier of the sample. [This should correspond to the lablel on the sample bottle].",
											"validate": "required"
										},
										{
											"dataType": "list",
											"name": "waterChemistryProperties",
											"allowRowDelete": false,
											"columns": [{
													"dataType": "text",
													"name": "measuredProperty",
													"description": "",
													"noEdit": true,
													"readOnly": true
												},
												{
													"dataType": "text",
													"name": "measuredValueQualifier",
													"defaultValue": "=",
													"constraints": [
														"<",
														"=",
														">"
													]
												},
												{
													"dataType": "number",
													"name": "measuredValue",
													"description": "The value measured for a given property in the default units of measurement for that property.",
													"validate": "min[0]"
												},
												{
													"dataType": "text",
													"name": "measurementMethod",
													"description": "The method used to make a given measurement",
													"constraints": [
														"Metals-020",
														"Metals-022",
														"Inorg-006",
														"Inorg-040",
														"Inorg-081"
													]
												},
												{
													"dataType": "number",
													"name": "measurementPql",
													"description": "",
													"validate": "min[0]"
												}
											],
											"defaultRows": [{
													"measuredProperty": "Calcium (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Potassium (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Sodium (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Magnesium (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Hardness (mgCaCo3/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Hydroxide Alkalinity (OH-) (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Bicarbonate Alkalinity (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Carbonate Alkalinity (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Total Alkalinity as CaCo3 (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Sulphate (SO4) (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Chloride (Cl) (mg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Ionic Balance (%)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Arsenic - Total (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Boron - Total (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Barium (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Beryllium - Total (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Cobalt - Total (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Copper (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Aluminium (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Iron - Total (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Manganese (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Lead (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Nickel (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Zinc (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Strontium (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Lithium (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												},
												{
													"measuredProperty": "Chromium (µg/L)",
													"measuredValueQualifier": "",
													"measuredValue": "",
													"measurementMethod": "",
													"measurementPql": ""
												}
											]
										}
									],
									"title": "BMWHI - Water Chemical Properties"
								}
							}
						}]
					}]
				}
			}]
		}]
	}
}''')

vegetation_health_survey = json.loads('''{"data":{"searchBioCollectProject":[{"projectId":"f72f7cbc-5ccd-480f-8a4c-0a9a3a5c9cae","name":"Blue Mountains Upland Swamps","sites":[{"siteId":"747ac352-6ad7-438e-905a-e7a8bc2533dc","name":"Project area for Blue Mountains Upland Swamps","externalSiteId":null,"type":"","catchment":"","status":"active","visibility":null,"siteGeojson":{"geometry":{"type":"Polygon","coordinates":["[[150.13366699218747, -33.50269783481254], [150.6719970703125, -33.628570663568816], [150.64727783203125, -33.91396172610034], [150.15014648437497, -33.761110320624105], [150.13366699218747, -33.50269783481254]]"]}}},{"siteId":"e7ce64a9-99dd-4009-bb94-dc8cf7d75746","name":"Grand Canyon Swamp Exit Stream","externalSiteId":null,"type":"monitoringPoint","catchment":"","status":"active","visibility":null,"siteGeojson":{"geometry":{"type":"Polygon","coordinates":["[[150.32015562057492, -33.66076032976858], [150.32097101211548, -33.660867489391755], [150.3197479248047, -33.66511804679502], [150.31882524490354, -33.66501089246613], [150.3186535835266, -33.66251058690082], [150.32015562057492, -33.66076032976858]]"]}}},{"siteId":"89030c0b-d965-428c-8bf0-ab165e74bf2e","name":"Private site for survey: Water table monitoring - piezometer recordings","externalSiteId":null,"type":null,"catchment":null,"status":"active","visibility":"private","siteGeojson":{"geometry":{"type":"Polygon","coordinates":["[[150.20166166126725, -33.741213210385865], [150.20264871418476, -33.738679434257975], [150.204494073987, -33.7364310913657], [150.20900018513203, -33.73707348106183], [150.20698316395283, -33.738500996498566], [150.20535238087177, -33.7408563450369], [150.20591028034687, -33.74249791334891], [150.2029062062502, -33.74264065693483], [150.2015758305788, -33.74246222741532], [150.20166166126725, -33.741213210385865]]"]}}},{"siteId":"b1c4f414-edd1-4c51-9c99-8c3149c5ead1","name":"Grand Canyon Swamp Piezometer","externalSiteId":null,"type":"surveyArea","catchment":"","status":"active","visibility":null,"siteGeojson":{"geometry":{"type":"Polygon","coordinates":["[[150.32114267349243, -33.664417969351916], [150.3196406364441, -33.665400219140835], [150.3185784816742, -33.66493588427473], [150.31943678855896, -33.66214982244585], [150.32015562057492, -33.662194471583966], [150.31997323036194, -33.66400720702358], [150.32114267349243, -33.664417969351916]]"]}}},{"siteId":"a2f70dd0-cbf6-4385-876d-d929baed584f","name":"Lawson Swamp Piezometer","externalSiteId":null,"type":"surveyArea","catchment":"","status":"active","visibility":null,"siteGeojson":{"geometry":{"type":"Polygon","coordinates":["[[150.42689681053162, -33.7149678272743], [150.4276478290558, -33.71527125443331], [150.42726159095764, -33.71724350482991], [150.42623162269592, -33.71696685705355], [150.42689681053162, -33.7149678272743]]"]}}},{"siteId":"23caa0cb-30c9-419b-9963-7056ec614fe5","name":"Lawson Swamp Culvert Exit Stream","externalSiteId":null,"type":"surveyArea","catchment":"","status":"active","visibility":null,"siteGeojson":{"geometry":{"type":"Polygon","coordinates":["[[150.42691826820374, -33.7149856759604], [150.42765855789185, -33.71524448149183], [150.42720794677734, -33.71733274585793], [150.4262101650238, -33.717207808392715], [150.4265856742859, -33.71592272676971], [150.42691826820374, -33.7149856759604]]"]}}},{"siteId":"4f494553-ec14-4197-837f-d5f502c21ed9","name":"Bullaburra Swamp Piezometer","externalSiteId":null,"type":"surveyArea","catchment":"","status":"active","visibility":null,"siteGeojson":{"geometry":{"type":"Polygon","coordinates":["[[150.41271328926086, -33.727038046362914], [150.41303515434265, -33.727154046444525], [150.4132229089737, -33.727814351615024], [150.4129761457443, -33.72790804315332], [150.41260600090027, -33.727336969331596], [150.41268646717072, -33.727038046362914], [150.41271328926086, -33.727020200182594], [150.41271328926086, -33.727038046362914]]"]}}},{"siteId":"e1460811-ad65-445e-a933-84fdb25728c3","name":"Bullaburra Swamp Exit Stream","externalSiteId":null,"type":"surveyArea","catchment":"","status":"active","visibility":null,"siteGeojson":{"geometry":{"type":"Polygon","coordinates":["[[150.41265964508057, -33.7270603540831], [150.4129707813263, -33.727100507964806], [150.41321218013763, -33.727814351615024], [150.41296005249023, -33.72792142765044], [150.41258990764618, -33.72718081567187], [150.41265964508057, -33.7270603540831]]"]}}}],"surveys":[{"surveyDetails":{"surveyMetadata":{"name":"Vegetation Health Survey","description":"This survey uses the simple photo protocol methodology to assess the extent and severity of bushfire impacts and to monitor the response and recovery of bushland areas following bushfire events. ","version":7,"methodType":"systematic","methodName":"Vegetation condition assessment - Post fire - Simple Photo Protocol","startDate":"2021-03-27","endDate":null,"pActivityFormName":"Bush After Fire","dataSharingLicense":"https://creativecommons.org/licenses/by/4.0/","legalCustodianOrganisation":"Blue Mountains World Heritage Institute","spatialAccuracy":"high","temporalAccuracy":"high","speciesIdentification":"na","nonTaxonomicAccuracy":"moderate","dataQualityAssuranceMethods":["dataownercurated","systemsupported"],"dataQualityAssuranceDescription":"","dataManagementPolicyDocument":"","status":"active","dataAccessExternalURL":"","isDataManagementPolicyDocumented":false,"sites":["e1460811-ad65-445e-a933-84fdb25728c3","4f494553-ec14-4197-837f-d5f502c21ed9","e7ce64a9-99dd-4009-bb94-dc8cf7d75746","b1c4f414-edd1-4c51-9c99-8c3149c5ead1","23caa0cb-30c9-419b-9963-7056ec614fe5","a2f70dd0-cbf6-4385-876d-d929baed584f"]},"surveyForms":[{"name":"Bush After Fire","version":10,"activationDate":null,"publicationStatus":"published","type":"Assessment","status":"active","formSections":[{"title":null,"name":"Bush After Fire","templateName":"bushAfterFire","formTemplate":{"sectionTemplate":{"modelName":"Bush After Fire","dataModel":[{"dataType":"image","name":"locationPhoto","validate":"required"},{"dataType":"text","name":"locationPhotoDirection","constraints":["North","South","East","West"],"validate":"required"},{"dataType":"text","name":"recordedBy","dwcAttribute":"recordedBy","description":"The person who made the observation.","validate":"required"},{"dataType":"date","name":"observationDate","dwcAttribute":"eventDate","defaultValue":"${now}","validate":"required"},{"dataType":"species","name":"treeSpecies","dwcAttribute":"scientificName","description":"Enter the name of the tree species, if known"},{"dataType":"text","name":"landuse","description":"Select the most appropriate category applying to the use of the land.","constraints":["Cropping","Grazing (improved paddock)","Grazing (unimproved paddock)","Native vegetation","Other rural","Urban - Private garden","Urban - Public space"]},{"dataType":"text","name":"topography","description":"Select the most appropriate category that describes the slope at the location.","constraints":["Ridge","Gully","Flat"]},{"dataType":"text","name":"locationDescription","description":""},{"dataType":"text","name":"recentFireHistoryBoolean","description":"Do you know if there was a fire recently at this location?","constraints":["Yes","No","Don't know"]},{"dataType":"text","name":"recentFireHistoryDate","description":"If you know that there was a fire recently at this location, do you know which year it occurred?","constraints":["2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004"]},{"dataType":"text","name":"previousObservation","description":"Has an observation of this kind previously been made at this location?","constraints":["Yes","No","Don't know"]},{"dataType":"text","name":"previousObservationDate","description":"If known, please indicate the year of the last observation at this location.","constraints":["2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004"]},{"dataType":"text","name":"observationRemarks","description":"Please add any additional notes or comments about the location or the visit which might be relevant."},{"dataType":"text","name":"contactAgreement","description":"Please indicate whether you are happy to be contacted by the project researchers about this record and whether you agree to the Atlas of Living Australia sharing your contact email address with the researchers for this purpose.","constraints":["Yes","No"],"validate":"required"},{"dataType":"image","name":"simplePhotoProtocolNorth","description":""},{"dataType":"image","name":"simplePhotoProtocolSouth","description":""},{"dataType":"image","name":"simplePhotoProtocolCanopy","description":""},{"dataType":"image","name":"simplePhotoProtocolSky","description":""},{"dataType":"image","name":"simplePhotoProtocolGround","description":""},{"dataType":"text","name":"severityClass","description":"","constraints":["Unburnt","Burnt grassland","Low Severity","Moderate Severity","High Severity","Extreme Severity"]},{"dataType":"text","name":"foliageProjectedCoverEstimateCategorical","description":"","constraints":["Low Cover <30%","Moderate Cover 30-70%","High Cover >70%"]},{"dataType":"text","name":"vegetationStructuralType","description":"","constraints":["Dry Sclerophyll","Wet Sclerophyll","Dry Heath","Wet Heath","Shrublands","Tall Shrublands >2m","Shrubby regrowth","Rock/rocky outcrop","Riparian forest/woodland","Rainforest","Open Grassy woodland","Grassland"]},{"dataType":"number","name":"scorchHeightAboveGroundInMetres","description":"The height above ground in metres to which there is evidence of recent scorching.","validate":"min[0],max[99]"},{"allowRowDelete":false,"allowHeaderWrap":true,"columns":[{"dataType":"text","name":"percentOfFireImpactClass","description":"","readOnly":true},{"dataType":"number","name":"vegetationLayerTrees","description":"","validate":"min[0],max[100]"},{"dataType":"number","name":"vegetationLayerSubCanopy","description":"","validate":"min[0],max[100]"},{"dataType":"number","name":"vegetationLayerShrubs","description":"","validate":"min[0],max[100]"},{"dataType":"number","name":"vegetationLayerGround","description":"","validate":"min[0],max[100]"}],"dataType":"list","name":"vegetationStructuretable","defaultRows":[{"vegetationLayerTrees_heightInMetres":"","vegetationLayerSubCanopy_heightInMetres":"","vegetationLayerShrubs_heightInMetres":"","vegetationLayerGround_heightInMetres":"","percentOfFireImpactClass":"Height of layer (m)"},{"vegetationLayerTrees_percentCoverLiving":"","vegetationLayerSubCanopy_percentCoverLiving":"","vegetationLayerShrubs_percentCoverLiving":"","vegetationLayerGround_percentCoverLiving":"","percentOfFireImpactClass":"% Cover of living vegetation"},{"vegetationLayerTrees_percentCoverScorched":"","vegetationLayerSubCanopy_percentCoverScorched":"","vegetationLayerShrubs_percentCoverScorched":"","vegetationLayerGround_percentCoverScorched":"","percentOfFireImpactClass":"% Cover of vegetation scorched (brown) but not fully consumed by fire"},{"vegetationLayerTrees_percentCoverFullyBurnt":"","vegetationLayerSubCanopy_percentCoverFullyBurnt":"","vegetationLayerShrubs_percentCoverFullyBurnt":"","vegetationLayerGround_percentCoverFullyBurnt":"","percentOfFireImpactClass":"% Cover of vegetation that would have been fully consumed by fire"}]},{"dataType":"text","name":"comments"},{"defaultAccuracy":50,"hideMyLocation":false,"columns":[{"dwcAttribute":"verbatimLatitude","source":"locationLatitude"},{"dwcAttribute":"verbatimLongitude","source":"locationLongitude"},{"source":"Locality"},{"source":"Accuracy"},{"source":"Notes"},{"source":"Source"}],"dataType":"geoMap","name":"location","dwcAttribute":"verbatimCoordinates","hideSiteSelection":true,"zoomToProjectArea":true,"validate":"required"}],"title":"Bush After Fire"}}}]}]}}]}]}}''')

water_table_and_water_physics_survey = json.loads('''{
	"data": {
		"searchBioCollectProject": [{
			"projectId": "f72f7cbc-5ccd-480f-8a4c-0a9a3a5c9cae",
			"name": "Blue Mountains Upland Swamps",
			"sites": [{
					"siteId": "747ac352-6ad7-438e-905a-e7a8bc2533dc",
					"name": "Project area for Blue Mountains Upland Swamps",
					"externalSiteId": null,
					"type": "",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.13366699218747, -33.50269783481254], [150.6719970703125, -33.628570663568816], [150.64727783203125, -33.91396172610034], [150.15014648437497, -33.761110320624105], [150.13366699218747, -33.50269783481254]]"
							]
						}
					}
				},
				{
					"siteId": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
					"name": "Grand Canyon Swamp Exit Stream",
					"externalSiteId": null,
					"type": "monitoringPoint",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.32015562057492, -33.66076032976858], [150.32097101211548, -33.660867489391755], [150.3197479248047, -33.66511804679502], [150.31882524490354, -33.66501089246613], [150.3186535835266, -33.66251058690082], [150.32015562057492, -33.66076032976858]]"
							]
						}
					}
				},
				{
					"siteId": "89030c0b-d965-428c-8bf0-ab165e74bf2e",
					"name": "Private site for survey: Water table monitoring - piezometer recordings",
					"externalSiteId": null,
					"type": null,
					"catchment": null,
					"status": "active",
					"visibility": "private",
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.20166166126725, -33.741213210385865], [150.20264871418476, -33.738679434257975], [150.204494073987, -33.7364310913657], [150.20900018513203, -33.73707348106183], [150.20698316395283, -33.738500996498566], [150.20535238087177, -33.7408563450369], [150.20591028034687, -33.74249791334891], [150.2029062062502, -33.74264065693483], [150.2015758305788, -33.74246222741532], [150.20166166126725, -33.741213210385865]]"
							]
						}
					}
				},
				{
					"siteId": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
					"name": "Grand Canyon Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.32114267349243, -33.664417969351916], [150.3196406364441, -33.665400219140835], [150.3185784816742, -33.66493588427473], [150.31943678855896, -33.66214982244585], [150.32015562057492, -33.662194471583966], [150.31997323036194, -33.66400720702358], [150.32114267349243, -33.664417969351916]]"
							]
						}
					}
				},
				{
					"siteId": "a2f70dd0-cbf6-4385-876d-d929baed584f",
					"name": "Lawson Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.42689681053162, -33.7149678272743], [150.4276478290558, -33.71527125443331], [150.42726159095764, -33.71724350482991], [150.42623162269592, -33.71696685705355], [150.42689681053162, -33.7149678272743]]"
							]
						}
					}
				},
				{
					"siteId": "23caa0cb-30c9-419b-9963-7056ec614fe5",
					"name": "Lawson Swamp Culvert Exit Stream",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.42691826820374, -33.7149856759604], [150.42765855789185, -33.71524448149183], [150.42720794677734, -33.71733274585793], [150.4262101650238, -33.717207808392715], [150.4265856742859, -33.71592272676971], [150.42691826820374, -33.7149856759604]]"
							]
						}
					}
				},
				{
					"siteId": "4f494553-ec14-4197-837f-d5f502c21ed9",
					"name": "Bullaburra Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.41271328926086, -33.727038046362914], [150.41303515434265, -33.727154046444525], [150.4132229089737, -33.727814351615024], [150.4129761457443, -33.72790804315332], [150.41260600090027, -33.727336969331596], [150.41268646717072, -33.727038046362914], [150.41271328926086, -33.727020200182594], [150.41271328926086, -33.727038046362914]]"
							]
						}
					}
				},
				{
					"siteId": "e1460811-ad65-445e-a933-84fdb25728c3",
					"name": "Bullaburra Swamp Exit Stream",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.41265964508057, -33.7270603540831], [150.4129707813263, -33.727100507964806], [150.41321218013763, -33.727814351615024], [150.41296005249023, -33.72792142765044], [150.41258990764618, -33.72718081567187], [150.41265964508057, -33.7270603540831]]"
							]
						}
					}
				}
			],
			"surveys": [{
				"surveyDetails": {
					"surveyMetadata": {
						"name": "Water Table and Water Physics",
						"description": "Piezometers have been established at each swamp to monitor fluctuations in the water table. These data are combined with other observations and measurements at these locations to assess the relationships between water table movement and other measured parameters.",
						"version": 24,
						"methodType": "systematic",
						"methodName": "Water table and water physics data collection",
						"startDate": "2021-03-27",
						"endDate": null,
						"pActivityFormName": "BMWHI - Piezometer Readings",
						"dataSharingLicense": "https://creativecommons.org/licenses/by/4.0/",
						"legalCustodianOrganisation": "Blue Mountains World Heritage Institute",
						"spatialAccuracy": "high",
						"temporalAccuracy": "high",
						"speciesIdentification": "na",
						"nonTaxonomicAccuracy": "high",
						"dataQualityAssuranceMethods": [
							"dataownercurated",
							"systemsupported"
						],
						"dataQualityAssuranceDescription": "",
						"dataManagementPolicyDocument": "",
						"status": "active",
						"dataAccessExternalURL": "",
						"isDataManagementPolicyDocumented": false,
						"sites": [
							"e1460811-ad65-445e-a933-84fdb25728c3",
							"4f494553-ec14-4197-837f-d5f502c21ed9",
							"e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
							"b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
							"23caa0cb-30c9-419b-9963-7056ec614fe5",
							"a2f70dd0-cbf6-4385-876d-d929baed584f",
							"747ac352-6ad7-438e-905a-e7a8bc2533dc"
						]
					},
					"surveyForms": [{
						"name": "BMWHI - Piezometer Readings",
						"version": 55,
						"activationDate": null,
						"publicationStatus": "published",
						"type": "Assessment",
						"status": "active",
						"formSections": [{
							"title": null,
							"name": "BMWHI - Piezometer Readings",
							"templateName": "bmwhiPiezometerReadings",
							"formTemplate": {
								"sectionTemplate": {
									"modelName": "BMWHI - Piezometer Readings",
									"dataModel": [{
											"dataType": "text",
											"description": "The name of the person who made the observation (edit the default name if appropriate).",
											"name": "recordedBy",
											"dwcAttribute": "recordedBy",
											"validate": "required"
										},
										{
											"dataType": "date",
											"description": "The date that the observation was made (this is not necessarily the date the record was entered into the database).",
											"name": "eventDate",
											"dwcAttribute": "eventDate",
											"defaultValue": "${now}",
											"validate": "required"
										},
										{
											"dataType": "time",
											"description": "The time that the recording was made.",
											"name": "eventTime",
											"dwcAttribute": "eventTime",
											"validate": "required"
										},
										{
											"dataType": "text",
											"name": "piezometerId",
											"description": "Unique identifier of the piezometer."
										},
										{
											"dataType": "number",
											"name": "dipDurationInMinutes",
											"dwcAttribute": "sampleSizeUnit",
											"description": "The average duration of time (in minutes) the sampling probe was submerged for the readings.",
											"validate": "min[0],max[10]"
										},
										{
											"dataType": "number",
											"name": "piezometerHeightAboveGroundInCentimetres",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterTableHeightInCentimetres",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "relativeWaterLevelDifferenceInCentimetres",
											"description": "The difference between the water table height and the fixed piezometer height in centimetres",
											"readOnly": true,
											"noEdit": true,
											"computed": {
												"dependents": [
													"piezometerHeightAboveGroundInCentimetres",
													"waterTableHeightInCentimetres"
												],
												"operation": "difference"
											},
											"primaryResult": "true",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "totalWaterDepthInCentimetres",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterPh_1",
											"description": "",
											"validate": "min[0],max[14]"
										},
										{
											"dataType": "number",
											"name": "waterPh_2",
											"description": "",
											"validate": "min[0],max[14]"
										},
										{
											"dataType": "number",
											"name": "waterPh_3",
											"description": "",
											"validate": "min[0],max[14]"
										},
										{
											"dataType": "number",
											"name": "waterPh_4",
											"description": "",
											"validate": "min[0],max[14]"
										},
										{
											"dataType": "number",
											"name": "waterPh_5",
											"description": "",
											"validate": "min[0],max[14]"
										},
										{
											"dataType": "number",
											"name": "waterElectricalConductivityInMicrosiemensPerCentimetre_1",
											"indexName": "waterElectricalConductivityInMicrosiemensPerCentimetre",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterElectricalConductivityInMicrosiemensPerCentimetre_2",
											"indexName": "waterElectricalConductivityInMicrosiemensPerCentimetre",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterElectricalConductivityInMicrosiemensPerCentimetre_3",
											"indexName": "waterElectricalConductivityInMicrosiemensPerCentimetre",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterElectricalConductivityInMicrosiemensPerCentimetre_4",
											"indexName": "waterElectricalConductivityInMicrosiemensPerCentimetre",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterElectricalConductivityInMicrosiemensPerCentimetre_5",
											"indexName": "waterElectricalConductivityInMicrosiemensPerCentimetre",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterTemperatureInDegreesCelcius_1",
											"indexName": "BMWHIwaterTemperatureInDegreesCelcius",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterTemperatureInDegreesCelcius_2",
											"indexName": "BMWHIwaterTemperatureInDegreesCelcius",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterTemperatureInDegreesCelcius_3",
											"indexName": "BMWHIwaterTemperatureInDegreesCelcius",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterTemperatureInDegreesCelcius_4",
											"indexName": "BMWHIwaterTemperatureInDegreesCelcius",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterTemperatureInDegreesCelcius_5",
											"indexName": "BMWHIwaterTemperatureInDegreesCelcius",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInPercentSaturation_1",
											"indexName": "BMWHIwaterDoPcSat",
											"description": "",
											"validate": "min[0],max[100]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInPercentSaturation_2",
											"indexName": "BMWHIwaterDoPcSat",
											"description": "",
											"validate": "min[0],max[100]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInPercentSaturation_3",
											"indexName": "BMWHIwaterDoPcSat",
											"description": "",
											"validate": "min[0],max[100]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInPercentSaturation_4",
											"indexName": "BMWHIwaterDoPcSat",
											"description": "",
											"validate": "min[0],max[100]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInPercentSaturation_5",
											"indexName": "BMWHIwaterDoPcSat",
											"description": "",
											"validate": "min[0],max[100]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInMilligramsPerLitre_1",
											"indexName": "BMWHIwaterDoMgl",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInMilligramsPerLitre_2",
											"indexName": "BMWHIwaterDoMgl",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInMilligramsPerLitre_3",
											"indexName": "BMWHIwaterDoMgl",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInMilligramsPerLitre_4",
											"indexName": "BMWHIwaterDoMgl",
											"description": "",
											"validate": "min[0]"
										},
										{
											"dataType": "number",
											"name": "waterDissolvedOxygenInMilligramsPerLitre_5",
											"indexName": "BMWHIwaterDoMgl",
											"description": "",
											"validate": "min[0]"
										},
										{
											"columns": [{
													"dwcAttribute": "verbatimLatitude",
													"source": "locationLatitude"
												},
												{
													"dwcAttribute": "verbatimLongitude",
													"source": "locationLongitude"
												},
												{
													"source": "Locality"
												},
												{
													"description": "",
													"source": "Accuracy"
												},
												{
													"description": "Describe the location. E.g. approximately 200m south of currency creek settlement at Lions Park walking trail entrance",
													"source": "Notes"
												},
												{
													"source": "Source"
												}
											],
											"dataType": "geoMap",
											"name": "location",
											"validate": "required"
										}
									],
									"title": "BMWHI - Piezometer Readings"
								}
							}
						}]
					}]
				}
			}]
		}]
	}
}''')

wetland_sediment_survey = json.loads('''{
	"data": {
		"searchBioCollectProject": [{
			"projectId": "f72f7cbc-5ccd-480f-8a4c-0a9a3a5c9cae",
			"name": "Blue Mountains Upland Swamps",
			"sites": [{
					"siteId": "747ac352-6ad7-438e-905a-e7a8bc2533dc",
					"name": "Project area for Blue Mountains Upland Swamps34",
					"externalSiteId": null,
					"type": "",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.13366699218747, -33.50269783481254], [150.6719970703125, -33.628570663568816], [150.64727783203125, -33.91396172610034], [150.15014648437497, -33.761110320624105], [150.13366699218747, -33.50269783481254]]"
							]
						}
					}
				},
				{
					"siteId": "e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
					"name": "Grand Canyon Swamp Exit Stream",
					"externalSiteId": null,
					"type": "monitoringPoint",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.32015562057492, -33.66076032976858], [150.32097101211548, -33.660867489391755], [150.3197479248047, -33.66511804679502], [150.31882524490354, -33.66501089246613], [150.3186535835266, -33.66251058690082], [150.32015562057492, -33.66076032976858]]"
							]
						}
					}
				},
				{
					"siteId": "89030c0b-d965-428c-8bf0-ab165e74bf2e",
					"name": "Private site for survey: Water table monitoring - piezometer recordings",
					"externalSiteId": null,
					"type": null,
					"catchment": null,
					"status": "active",
					"visibility": "private",
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.20166166126725, -33.741213210385865], [150.20264871418476, -33.738679434257975], [150.204494073987, -33.7364310913657], [150.20900018513203, -33.73707348106183], [150.20698316395283, -33.738500996498566], [150.20535238087177, -33.7408563450369], [150.20591028034687, -33.74249791334891], [150.2029062062502, -33.74264065693483], [150.2015758305788, -33.74246222741532], [150.20166166126725, -33.741213210385865]]"
							]
						}
					}
				},
				{
					"siteId": "b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
					"name": "Grand Canyon Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.32114267349243, -33.664417969351916], [150.3196406364441, -33.665400219140835], [150.3185784816742, -33.66493588427473], [150.31943678855896, -33.66214982244585], [150.32015562057492, -33.662194471583966], [150.31997323036194, -33.66400720702358], [150.32114267349243, -33.664417969351916]]"
							]
						}
					}
				},
				{
					"siteId": "a2f70dd0-cbf6-4385-876d-d929baed584f",
					"name": "Lawson Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.42689681053162, -33.7149678272743], [150.4276478290558, -33.71527125443331], [150.42726159095764, -33.71724350482991], [150.42623162269592, -33.71696685705355], [150.42689681053162, -33.7149678272743]]"
							]
						}
					}
				},
				{
					"siteId": "23caa0cb-30c9-419b-9963-7056ec614fe5",
					"name": "Lawson Swamp Culvert Exit Stream",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.42691826820374, -33.7149856759604], [150.42765855789185, -33.71524448149183], [150.42720794677734, -33.71733274585793], [150.4262101650238, -33.717207808392715], [150.4265856742859, -33.71592272676971], [150.42691826820374, -33.7149856759604]]"
							]
						}
					}
				},
				{
					"siteId": "4f494553-ec14-4197-837f-d5f502c21ed9",
					"name": "Bullaburra Swamp Piezometer",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.41271328926086, -33.727038046362914], [150.41303515434265, -33.727154046444525], [150.4132229089737, -33.727814351615024], [150.4129761457443, -33.72790804315332], [150.41260600090027, -33.727336969331596], [150.41268646717072, -33.727038046362914], [150.41271328926086, -33.727020200182594], [150.41271328926086, -33.727038046362914]]"
							]
						}
					}
				},
				{
					"siteId": "e1460811-ad65-445e-a933-84fdb25728c3",
					"name": "Bullaburra Swamp Exit Stream",
					"externalSiteId": null,
					"type": "surveyArea",
					"catchment": "",
					"status": "active",
					"visibility": null,
					"siteGeojson": {
						"geometry": {
							"type": "Polygon",
							"coordinates": [
								"[[150.41265964508057, -33.7270603540831], [150.4129707813263, -33.727100507964806], [150.41321218013763, -33.727814351615024], [150.41296005249023, -33.72792142765044], [150.41258990764618, -33.72718081567187], [150.41265964508057, -33.7270603540831]]"
							]
						}
					}
				}
			],
			"surveys": [

				{
					"surveyDetails": {
						"surveyMetadata": {
							"name": "Wetland Sediment Survey",
							"description": "Sediment cores are taken from wetlands and analysed for a range of properties relevant to determining the condition of the wetland environment.",
							"version": 6,
							"methodType": "systematic",
							"methodName": "Sediment core sampling",
							"startDate": "2021-03-27",
							"endDate": null,
							"pActivityFormName": "BMWHI - Wetland Sediment Survey",
							"dataSharingLicense": "https://creativecommons.org/licenses/by/4.0/",
							"legalCustodianOrganisation": "Blue Mountains World Heritage Institute",
							"spatialAccuracy": "high",
							"temporalAccuracy": "high",
							"speciesIdentification": "na",
							"nonTaxonomicAccuracy": "moderate",
							"dataQualityAssuranceMethods": [
								"dataownercurated",
								"systemsupported"
							],
							"dataQualityAssuranceDescription": "",
							"dataManagementPolicyDocument": "",
							"status": "active",
							"dataAccessExternalURL": "",
							"isDataManagementPolicyDocumented": false,
							"sites": [
								"e1460811-ad65-445e-a933-84fdb25728c3",
								"4f494553-ec14-4197-837f-d5f502c21ed9",
								"e7ce64a9-99dd-4009-bb94-dc8cf7d75746",
								"b1c4f414-edd1-4c51-9c99-8c3149c5ead1",
								"23caa0cb-30c9-419b-9963-7056ec614fe5",
								"a2f70dd0-cbf6-4385-876d-d929baed584f"
							]
						},
						"surveyForms": [{
							"name": "BMWHI - Wetland Sediment Survey",
							"version": 10,
							"activationDate": null,
							"publicationStatus": "published",
							"type": "Assessment",
							"status": "active",
							"formSections": [{
								"title": null,
								"name": "BMWHI - Wetland Sediment Survey",
								"templateName": "bmwhiWetlandSedimentSurvey",
								"formTemplate": {
									"sectionTemplate": {
										"modelName": "Wetland Sediment Survey",
										"dataModel": [{
												"dataType": "text",
												"description": "The name of the person who made the observation (edit the default name if appropriate).",
												"name": "recordedBy",
												"dwcAttribute": "recordedBy",
												"validate": "required"
											},
											{
												"dataType": "date",
												"description": "The date that the observation was made (this is not necessarily the date the record was entered into the database).",
												"name": "eventDate",
												"dwcAttribute": "eventDate",
												"defaultValue": "${now}",
												"validate": "required"
											},
											{
												"dataType": "text",
												"name": "eventRemarks",
												"description": "General observational notes applicable to the site, conditions, sampling undertaken, etc.",
												"dwcAttribute": "eventRemarks"
											},
											{
												"columns": [{
														"dwcAttribute": "verbatimLatitude",
														"source": "locationLatitude"
													},
													{
														"dwcAttribute": "verbatimLongitude",
														"source": "locationLongitude"
													},
													{
														"source": "Locality"
													},
													{
														"description": "",
														"source": "Accuracy"
													},
													{
														"description": "Describe the location. E.g. approximately 200m south of currency creek settlement at Lions Park walking trail entrance",
														"source": "Notes"
													},
													{
														"source": "Source"
													}
												],
												"dataType": "geoMap",
												"name": "location",
												"validate": "required"
											},
											{
												"dataType": "text",
												"name": "coreId",
												"description": "Unique identifier of the sample core.",
												"validate": "required"
											},
											{
												"dataType": "image",
												"name": "corePhoto",
												"description": "Upload a photo of the total sample core taken for this record."
											},
											{
												"dataType": "number",
												"name": "clayStackDepthInCentimetres",
												"description": "The depth of the clay layer in centimetres.",
												"validate": "min[0],integer"
											},
											{
												"dataType": "number",
												"name": "peatStackDepthInCentimetres",
												"description": "The depth of the peat layer in centimetres.",
												"validate": "min[0],integer"
											},
											{
												"dataType": "number",
												"name": "alternatingOrganicSandLayerThicknessInCentimetres",
												"description": "The thickness in centimetres of the alternating organic sand (AOS) layer in centimetres.",
												"validate": "min[0],integer"
											},
											{
												"dataType": "text",
												"name": "contemporarySandLayerPresent",
												"description": "Does a contemporary sand layer occur within the sampled profile?",
												"validate": "required",
												"constraints": [
													"Yes",
													"No"
												]
											},
											{
												"columns": [{
														"dataType": "text",
														"name": "subSampleReplicateId",
														"description": "Unique identifier of the core sub-sample preplicate.",
														"validate": "required"
													},
													{
														"dataType": "number",
														"name": "subSampleDepthInCentimetres",
														"description": "The total depth in centimetres of the core sub-sample measured.",
														"validate": "min[0],integer"
													},
													{
														"dataType": "number",
														"name": "subSampleSedimentPhMeasurement",
														"description": "The measured pH of the sediment in the core sub-sample.",
														"validate": "min[0],max[14]"
													},
													{
														"dataType": "number",
														"name": "subSampleCarbon",
														"description": " of the core sub-sample measured.",
														"validate": "min[0],integer"
													},
													{
														"dataType": "number",
														"name": "subSampleGrainSizeInMilimetres",
														"description": " of the core sub-sample measured.",
														"validate": "min[0],integer"
													}
												],
												"dataType": "list",
												"name": "sedimentSubSampleRepeatSection"
											}
										],
										"title": "Wetland Sediment Survey"
									}
								}
							}]
						}]
					}
				}
			]
		}]
	}
}''')
