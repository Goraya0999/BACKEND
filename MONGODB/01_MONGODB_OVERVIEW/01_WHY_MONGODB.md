# MongoDB 

## Why MongoDB?

MongoDB is a modern database used for building applications.
It provides important database features like:

* Transactions
* Indexing
* Fast query performance
* Strong security
* Flexible document structure

MongoDB uses a **document model**, which makes development easier and faster.

---

# Main Problem MongoDB Solves

Example: Product Catalog System

A product system may receive data from:

* Spreadsheets
* APIs
* Vendor systems

Each source may have:

* Different formats
* Missing data
* Different field names

Traditional databases need:

* Strict schemas
* Multiple tables
* Complex ETL pipelines
* Schema migrations

This increases:

* Development time
* Complexity
* Maintenance work

---

# How MongoDB Helps

MongoDB stores data as **BSON documents**
(BSON = Binary JSON format)

Each document can contain:

* Nested objects
* Arrays
* Different field structures

Example:
Different products can have different attributes without changing the database structure.

Benefits:

* Flexible data storage
* Faster development
* Easy to add new fields
* Less schema migration work

Important Idea:

> Your application can grow with the data.

---

# Data Modeling in MongoDB

MongoDB supports two relationship methods:

## 1. Embedded Data

Store related data inside one document.

Best for:

* Fast reads
* Atomic operations

## 2. Referenced Data

Store related data in separate collections.

Best for:

* Large datasets
* Different access patterns

MongoDB also supports:

* Nested field indexing
* Array indexing
* Query optimization

---

# MongoDB Production Features

## Replica Sets (High Availability)

MongoDB uses **Replica Sets**.

Replica sets:

* Keep multiple copies of data
* Automatically recover from failures

If the main server fails:

* MongoDB automatically switches to another server
* Minimal downtime
* No manual work needed

---

# MongoDB Atlas

## MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas?utm_source=chatgpt.com)

Atlas is MongoDB’s cloud database service.

Features:

* Fully managed database
* Automatic scaling
* Automatic patching
* Multi-cloud support
* Multi-region deployment

Benefits:

* Easier management
* Better reliability
* Better disaster protection

---

# Backup and Recovery

MongoDB provides:

* Automated backups
* Point-in-time recovery

This helps recover data after:

* Accidental deletion
* Bugs
* Infrastructure failures

---

# Monitoring and Observability

MongoDB includes built-in monitoring.

It tracks:

* Performance
* Availability
* Replication lag
* Resource usage

MongoDB alerts teams before problems affect users.

---

# Security Features

MongoDB provides enterprise-level security:

* Access control
* Encryption
* Field-level encryption
* Auditing
* LDAP integration
* SAML integration

Data is protected:

* In transit
* At rest

This helps companies meet compliance requirements.

---

# Scaling in MongoDB

MongoDB supports two scaling methods.

## 1. Vertical Scaling

Increase:

* CPU
* RAM
* Storage

Good for:

* Small to medium workloads

Atlas can automatically scale resources.

---

## 2. Horizontal Scaling (Sharding)

When applications grow very large, MongoDB uses **Sharding**.

Sharding:

* Splits data across multiple servers
* Improves performance
* Handles massive datasets

Important Components:

* Shards → store data
* Replica Sets → provide fault tolerance
* MongoS → query router

Benefits:

* Native scaling support
* No major application code changes

---

# Key Important Points

## MongoDB Advantages

* Flexible document model
* Easy schema changes
* Fast development
* High availability
* Built-in security
* Automatic failover
* Backup and recovery
* Monitoring tools
* Horizontal scaling with sharding
* Cloud support with Atlas

---


# Architecture Overview

![MongoDB Architecture](asset/image.png)
