---
tags: [baseten, organization]
source: https://docs.baseten.co/organization/restricted-environments
---

> Control access to sensitive environments like production with environment-level permissions.

Restricted environments let organization Admins lock down specific environments so that
only designated users can modify settings and configurations.
Use restricted environments to prevent unauthorized changes to critical
environments like production.

For more information on user roles, see
[[Access control]] and
[[Environments]].

## How restricted environments work

By default, environments are unrestricted, meaning any organization member can modify
deployments, autoscaling settings, and other configurations.
When you mark an environment as restricted, only users you explicitly grant access can
make changes.

Restricted environments apply across all models and Chains in your organization.
For example, if you restrict an environment named `production`, that restriction applies to
every model and chain's production environment, not just one specific model or chain.

> **Note:**
  If your organization uses [[Teams|teams]], restricted environments are scoped to individual teams.
  Team Admins can create and manage restricted environments for their team.

> **Note:**
  If your organization uses [[SSO and SCIM|SCIM]], an Organization Admin can also grant directory groups access to a restricted environment, in addition to individual users.

### Permissions by access level

| Action                                 | With access | Without access |
| :------------------------------------- | ----------- | -------------- |
| View environment and configuration     | ✅           | ✅ (read-only)  |
| View metrics                           | ✅           | ✅ (read-only)  |
| Call inference on models and chains    | ✅           | ✅              |
| View logs                              | ✅           | ✅              |
| Modify deployment settings             | ✅           | ❌              |
| Change autoscaling configurations      | ✅           | ❌              |
| Promote deployments to the environment | ✅           | ❌              |
| Manage environment-specific settings   | ✅           | ❌              |

Users without access see a grayed-out UI for restricted actions.
They retain full read access and can still call inference endpoints.

## Manage restricted environments

Only organization **Admins** can create or modify restricted environments.
Members (non-admin users) can only create unrestricted environments and can't change
environment restrictions.

### From the environments page

1. Navigate to **Settings** and then choose **Environments**.
2. Select an existing environment to modify, or select **Create environment** to create a new one.
3. Set the access level to **Restricted**.
4. Add users by searching by name or by email.
5. Select **Save changes** or **Create environment**.

### From a model or chain

1. Go to your model or chain's management page.
2. Select an existing environment to modify, or select **Add environment** then **Create environment** to create a new one.
3. Set the access level to **Restricted**.
4. Add users by searching by name or by email.
5. Select **Save changes** or **Create environment**.

> **Note:**
  Only admins can create restricted environments, and all admins have implicit
  access to every restricted environment. If an admin is later demoted to a member
  role, they lose this implicit access and can be removed from the environment
  like any other member.

### With the management API

You can read and update restriction settings programmatically through the [[List environment groups|environment groups endpoints]]. Each environment group carries a `manage_access` object with its restriction state and the users granted access.

## Regional environments

When you create a restricted environment, you can further work with Baseten to add regional restrictions that guarantee inference traffic stays within a designated geographic region. [Contact support](mailto:support@baseten.co) to configure regional restrictions for your environments. See [[Regional environments]] for more details.

## API behavior

Restricted environments apply the same permission checks to
[[Create environment|API]] and
[[truss push|truss CLI]] operations as the UI. API keys inherit
the permissions of their associated user.

If you attempt to modify a restricted environment using an API key associated with a
user without access, you'll receive a `403 Forbidden` error.

This includes operations like:

* Promoting deployments through the
  [[Promote to model environment|promote endpoint]].

* Updating autoscaling settings through the
  [[Any model deployment by ID|autoscaling endpoint]].

* Modifying environment configurations through the
  [[Update model environment|update environment endpoint]].

Users without access can still call inference endpoints, as restrictions only apply to
management operations.

---
Part of [[Organization Hub]]
