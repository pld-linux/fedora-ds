#
# http://directory.fedora.redhat.com/wiki/Building
#
Summary:	Fedora Directory Server
Summary(pl):	Fedora Directory Server - serwer us�ug katalogowych
Name:		fedora-ds
Version:	1.0.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	d8bd5b68087229b4bb2e3867cb92ba85
URL:		http://directory.fedora.redhat.com/
#BuildRequires:	apr-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel >= 4.0
# fake, but required now
BuildRequires:	db-utils
BuildRequires:	fedora-adminutil
BuildRequires:	fedora-setuputil
BuildRequires:	gdbm-devel >= 1.6
#BuildRequires:	java-sun
#BuildRequires:	libgssapi-devel
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtermcap-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	mozldap-devel >= 5.16
BuildRequires:	ncurses-devel
BuildRequires:	net-snmp-devel >= 5.2.1
BuildRequires:	nspr-devel >= 4.4.1
BuildRequires:	nss-devel >= 3.9.3
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	which
BuildRequires:	zip
#or BuildRequires:	ibm-java-sdk
#
#BuildRequires:	Java/XML Components
# axis.jar, jaxrpc.jar, and saaj.jar - http://ws.apache.org/axis/index.html
# xercesImpl.jar and xml-apis.jar - http://xml.apache.org/xerces2-j/download.cgi
# activation.jar - http://java.sun.com/products/javabeans/glasgow/jaf.html
# axrpc-api.jar - http://java.sun.com/webservices/downloads/webservicespack.html
# crimson.jar - http://xml.apache.org/dist/crimson/
#BuildRequires:	apache-devel
#BuildRequires:	jakarta-ant >= 1.6.1
#BuildRequires:	krb5-devel
#BuildRequires:	mozilla-components: DBM (v1.61), NSS (v3.93), SVRCORE (v4.0), LDAPSDK (v5.16), and PerLDAP (*)
#BuildRequires:	perl-Mozilla-LDAP
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
Fedora Directory Server to pot�ny, posiadaj�cy otwarte �r�d�a,
skalowalny serwer zaprojektowany do zarz�dzania du�ymi katalogami
u�ytkownik�w i zasob�w. Jest oparty na otwartym protokole serwerowym
LDAP (Lightweight Directory Access Protocol). Fedora Directory Server
to �wiatowej klasy implementacja serwera us�ug katalogowych. Bardziej
interesuj�ce cechy obejmuj�:
- 4-stronn� replikacj� multi-master
- skalowalno��: tysi�ce operacji na sekund�, dziesi�tki tysi�cy
  jednoczesnych u�ytkownik�w, dziesi�tki milion�w wpis�w, setki
  gigabajt�w danych
- obs�ug� SSLv3, TLSv1 i SASL do bezpiecznego uwierzytelniania i
  przesy�ania danych
- obs�ug� wi�kszo�ci cech LDAPv3, w tym wielu popularnych opcji i
  rozszerze�
- uaktualnianie schematu przez LDAP
- elastyczne informacje o prawach dost�pu w drzewie (ACI - Access
  Control Information), uaktualniane przez LDAP
- konfiguracj� i zarz�dzanie w locie przez LDAP
- graficzn� konsol� dla wszystkich aspekt�w zarz�dzania u�ytkownikami,
  grupami i serwerem

%prep
%setup -q
# dirty hack, maybe fedora-adminserver needed
mkdir -p __admserv/admin
touch __admserv/setup.inf

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	MAKE=%{__make} \
	ADMINUTIL_INCPATH=%{_includedir}/libadminutil \
	ADMINUTIL_LINK=-ladminutil10 \
	ADMINSERVER_SUBCOMPS=setup.inf \
	ADMSERV_DIR=$PWD/__admserv \
	DB_BINPATH=%{_bindir} \
	DB_INCLUDE=%{_includedir} \
	DBM_INCDIR=%{_includedir} \
	DBM_LIBNAMES=gdbm \
	GSSAPI_LIBS=-lgssapi \
	ICU_INCDIR=%{_includedir}/unicode \
	ICU_INCPATH=%{_includedir}/icu \
	LDAPSDK_INCDIR=%{_includedir}/mozldap \
	NETSNMP_INCDIR=%{_includedir}/net-snmp \
	NETSNMP_LIBNAMES="netsnmp netsnmpagent netsnmpmibs netsnmphelpers rpm sensors" \
	NSPR_INCDIR=%{_includedir}/nspr \
	SASL_INCDIR=%{_includedir}/sasl \
	SECURITY_INCDIR=%{_includedir}/nss \
	SETUPUTIL_INCDIR=%{_includedir} \
	SETUPUTIL_BINPATH=%{_bindir} \
	SVRCORE_INCLUDE=-I$PWD/../mozilla/security/svrcore \
	MFLAGS="\
		USE_ADMINSERVER=1 \
		USE_CONSOLE=0 \
		USE_DSMLGW=0 \
		USE_ORGCHART=1 \
		USE_DSGW=1 \
		USE_JAVATOOLS=0 \
		USE_SETUPUTIL=1 \
		USE_PERL_FROM_PATH=1 \
		DEBUG=full \
		NOJAVA=1"

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
