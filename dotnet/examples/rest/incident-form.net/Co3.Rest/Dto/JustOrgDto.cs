/*
 * Resilient Systems, Inc. ("Resilient") is willing to license software
 * or access to software to the company or entity that will be using or
 * accessing the software and documentation and that you represent as
 * an employee or authorized agent ("you" or "your") only on the condition
 * that you accept all of the terms of this license agreement.
 *
 * The software and documentation within Resilient's Development Kit are
 * copyrighted by and contain confidential information of Resilient. By
 * accessing and/or using this software and documentation, you agree that
 * while you may make derivative works of them, you:
 *
 * 1)  will not use the software and documentation or any derivative
 *     works for anything but your internal business purposes in
 *     conjunction your licensed used of Resilient's software, nor
 * 2)  provide or disclose the software and documentation or any
 *     derivative works to any third party.
 *
 * THIS SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL RESILIENT BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 */

using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace Co3.Rest.Dto
{
    /// <summary>
    ///  Information about an organization.
    /// </summary>
    public class JustOrgDto
    {

        /// <summary>
        ///  The ID of the organization.
        /// </summary>
        [JsonProperty("id")]
        public int Id { get; set; }

        /// <summary>
        ///  The name of the organization.
        /// </summary>
        [JsonProperty("name")]
        public string Name { get; set; }

        /// <summary>
        ///  The address of the organization (e.g. "123 Main Street").
        /// </summary>
        [JsonProperty("addr")]
        public string Addr { get; set; }

        /// <summary>
        ///  A second address line (e.g. "Suite 234").
        /// </summary>
        [JsonProperty("addr2")]
        public string Addr2 { get; set; }

        /// <summary>
        ///  The city where the organization is located.
        /// </summary>
        [JsonProperty("city")]
        public string City { get; set; }

        /// <summary>
        ///  The state where the organization is located (free-form text).
        /// </summary>
        [JsonProperty("state")]
        public string State { get; set; }

        /// <summary>
        ///  The ZIP/postal code where the organization is located.
        /// </summary>
        [JsonProperty("zip")]
        public string Zip { get; set; }

        /// <summary>
        ///  Are attachments enabled for the organization?
        /// </summary>
        [JsonProperty("attachments_enabled")]
        public bool AttachmentsEnabled { get; set; }

        /// <summary>
        ///  Are tasks created as "private" (no members) by default?
        /// </summary>
        [JsonProperty("tasks_private")]
        public bool TasksPrivate { get; set; }

        /// <summary>
        ///  Are there SAML federations enabled for this organization?
        /// </summary>
        [JsonProperty("has_saml")]
        public bool HasSaml { get; set; }

        /// <summary>
        ///  Is SAML *required* for authentication into this organization?
        /// </summary>
        [JsonProperty("require_saml")]
        public bool RequireSaml { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty("twofactor_auth_domain")]
        public TwoFactorAuthDomainDto TwoFactorAuthDomain { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty("has_available_twofactor")]
        public bool HasAvailableTwoFactor { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty("authorized_ldap_group")]
        public string AuthorizedLdapGroup { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty("supports_ldap")]
        public bool SupportsLdap { get; set; }

        public override string ToString()
        {
            return Name;
        }
    }
}
