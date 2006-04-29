#
# http://directory.fedora.redhat.com/wiki/Building
#
Summary:	Fedora Directory Server
Summary(pl):	Fedora Directory Server - serwer us³ug katalogowych
Name:		fedora-ds
Version:	1.0.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	d8bd5b68087229b4bb2e3867cb92ba85
Patch0:		%{name}-make.patch
Patch1:		%{name}-included.patch
Patch2:		http://directory.fedora.redhat.com/sources/ldapserver-gcc4.patch
URL:		http://directory.fedora.redhat.com/
BuildRequires:	apr-devel
BuildRequires:	db-devel >= 4.0
BuildRequires:	java-sun
BuildRequires:	libicu-devel
BuildRequires:	libtermcap-devel
BuildRequires:	ncurses-devel
BuildRequires:	nspr-devel >= 4.4.1
BuildRequires:	rpmbuild(macros) >= 1.228
#or BuildRequires:	ibm-java-sdk
#
#BuildRequires:	Java/XML Components
# axis.jar, jaxrpc.jar, and saaj.jar - http://ws.apache.org/axis/index.html
# xercesImpl.jar and xml-apis.jar - http://xml.apache.org/xerces2-j/download.cgi
# activation.jar - http://java.sun.com/products/javabeans/glasgow/jaf.html
# axrpc-api.jar - http://java.sun.com/webservices/downloads/webservicespack.html
# crimson.jar - http://xml.apache.org/dist/crimson/
BuildRequires:	apache-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gdbm-devel >= 1.6
BuildRequires:	jakarta-ant >= 1.6.1
BuildRequires:	krb5-devel
#BuildRequires:	mozilla-components: DBM (v1.61), NSS (v3.93), SVRCORE (v4.0), LDAPSDK (v5.16), and PerLDAP (*)
BuildRequires:	net-snmp-devel >= 5.2.1
BuildRequires:	nss-devel
BuildRequires:	perl-Mozilla-LDAP
BuildRequires:	mozldap-devel
Requires:	libicu >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fedora Directory Server is a robust, scalable open-source server
designed to manage large directories of users and resources. It is
based on an open-systems server protocol called the Lightweight
Directory Access Protocol (LDAP). The Fedora Directory Server is a
world-class Directory Server implementation. Some of the more
interesting features that are included are:
- 4-Way Multi-Master Replication
- Scalability: thousands of operations per second, tens of thousands
  of concurrent users, tens of millions of entries, hundreds of
  gigabytes of data
- SSLv3, TLSv1, and SASL for secure authentication and transport
- Support for most LDAPv3 features, including many common controls and
  extensions
- Schema update over LDAP
- Flexible in-tree Access Control Information (ACIs), updatable over
  LDAP
- On-line configuration and management over LDAP
- Graphical console for all facets of user, group, and server
  management

%description -l pl
Fedora Directory Server to potê¿ny, posiadaj±cy otwarte ¼ród³a,
skalowalny serwer zaprojektowany do zarz±dzania du¿ymi katalogami
u¿ytkowników i zasobów. Jest oparty na otwartym protokole serwerowym
LDAP (Lightweight Directory Access Protocol). Fedora Directory Server
to ¶wiatowej klasy implementacja serwera us³ug katalogowych. Bardziej
interesuj±ce cechy obejmuj±:
- 4-stronn± replikacjê multi-master
- skalowalno¶æ: tysi±ce operacji na sekund±, dziesi±tki tysiêcy
  jednoczesnych u¿ytkowników, dziesi±tki milionów wpisów, setki
  gigabajtów danych
- obs³ugê SSLv3, TLSv1 i SASL do bezpiecznego uwierzytelniania i
  przesy³ania danych
- obs³ugê wiêkszo¶ci cech LDAPv3, w tym wielu popularnych opcji i
  rozszerzeñ
- uaktualnianie schematu przez LDAP
- elastyczne informacje o prawach dostêpu w drzewie (ACI - Access
  Control Information), uaktualniane przez LDAP
- konfiguracjê i zarz±dzanie w locie przez LDAP
- graficzn± konsolê dla wszystkich aspektów zarz±dzania u¿ytkownikami,
  grupami i serwerem

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1

%build
#%%configure
%{__make} \
	NSPR_INCDIR=/usr/include/nspr \
	SECURITY_INCDIR=/usr/include/openssl \
	DBM_INCLUDE=/usr/include \
	LDAP_INCLUDE=/usr/include/nss \
	SASL_INCLUDE=/usr/include/sasl \
	SVRCORE_INCLUDE=/usr/include \
	MFLAGS="\
		USE_ADMINSERVER=1 \
		USE_CONSOLE=1 \
		USE_DSMLGW=1 \
		USE_ORGCHART=1 \
		USE_DSGW=1 \
		USE_JAVATOOLS=1 \
		USE_SETUPUTIL=1 \
		BUILD_RPM=0 \
		DEBUG=full \
		NOJAVA=0 \
	"
#
#	BUILD_RPM=1 to make a RHEL/Fedora Core RPM package (default is a setuputil installable package).
#	DEBUG=full to build the debug version (default is optimized).
#	NOJAVA=1 to skip the Java code, including the console and DSML gateway.
#	USE_ADMINSERVER=1 - bundle the Admin Server (required to run Console/webapps)
#		USE_CONSOLE=1	- bundle the Administration Console (requires Java)
#		USE_DSMLGW=1	 - build/bundle the DSMLv2 Gateway (requires Java)
#		USE_ORGCHART=1   - build/bundle the Org Chart webapp
#		USE_DSGW=1	   - build/bundle the Phonebook/DS Gateway webapp
#		USE_JAVATOOLS=1  - build/bundle the Java command line tools
#		USE_SETUPUTIL=1  - build/bundle programs that use Setuputil
#

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
