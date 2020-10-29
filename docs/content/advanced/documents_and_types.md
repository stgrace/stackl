---
title: Documents and Types
kind: advanced
weight: 3
date: 2020-02-10 01:00:00 +0100
publishdate: 2020-02-01 00:00:00 +0000
expirydate: 2030-01-01 00:00:00 +0000
draft: false
tags: []
---
A Document is a Key/Value text-file in the JSON or YAML format that models IT infrastructure building blocks, application service definitions, and their configuration data.
Documents are the core unit through which STACKL understands the user's IT environment and does work: nearly every task will, in some way, affect documents.
This can be storing, changing, or deleting models of the IT infrastructure, submitting  application or service descriptions, instantiating and representing running applications, and so on.
Documents belong to one of two broad categories and are strictly typed.

## Categories

There are two categories of documents: **items** and **configs**.
Configs represent documents that model or describe elements or concepts of the user's IT environment and are files that by themselves are not actionable but serve as configuration.
Items are documents that are tangible elements of a user's IT environment, namely files that are actionable or represent an interactive entity, and commonly form the data that serves as input for orchestration tools.
Items can be the result of processing other documents.
For instance, a deployable piece of hardware (i.e., infrastructure target) described by a document is an item and can be the result of a user's environment, zone, and location documents which together uniquely represent that hardware.
In terms of how they are created, configs are always user-submitted direct models or descriptions of things to be used by STACKL and thus are stand-alone and not the result of other documents.
Items, in contrast, are actionable elements that are either submitted or generated by STACKL and so can be the result of other documents.

## Types

### Configs

**Environment**
: represents an environment used within your IT infrastructure; production, testing,

**Location**
: represents a logical (or physical) location used where the IT infrastructure is present; a description of the geographical location such as a city, a region, ...

**Zone**
: represents a logical network, security zone, or direct IT environment used within the location IT infrastructure; subnets, clusters, security groups, actual devices, etc

**Stack_Infrastructure_Template**
: models IT infrastructure as infrastructure targets originating from the environment, location, and zone and possessing a set of infrastructure capabilities

**Stack_Application_Template**
: models the application as a set of services with their requirements and policies

**Functional_Requirement**
: configuration packages required of the operating environment for the service to perform its functions

**Resource_Requirement**
: hardware resource requirements to run the service such as CPU, memory, hard disk capacity, ...

**Policy_Template**
: service- and application-level requirements that specify additional requirements on the service or applications, such as replicas, service latency links, availability conditions, ...

**Authentication**
: TODO

### Items

**Stack_Template**
: a template for possible stacks as a deployable set of services matched to suitable infrastructure targets.
A result of the processing of a SIT and a SAT to a set of workload placement solutions valid for that point in time

**Stack_Instance**
: an instantiation of one of the viable solutions of a ST on the IT infrastructure

**Infrastructure_Target**
: a virtual or physical entity capable of executing software (clusters, virtual machines, desktop computers, ...), that can be targeted to run services

**Service**
: Software entity that performs a small piece of functionality and has a clear set of service requirements