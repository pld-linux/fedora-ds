#
# http://directory.fedora.redhat.com/wiki/Building
#
Summary:	Fedora Directory Server
Summary(pl):	Fedora Directory Server - serwer us³ug katalogowych
Name:		fedora-ds
Version:	1.0.4
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	fca8c94d2bfdc3a762c0e8b09ab04b09
URL:		http://directory.fedora.redhat.com/
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	db-devel >= 4.0
# fake, but required now
#BuildRequires:	db-utils
BuildRequires:	fedora-adminutil >= 1.0
BuildRequires:	fedora-setuputil >= 1.0
BuildRequires:	gdbm-devel >= 1.6
#BuildRequires:	java-sun
#BuildRequires:	libgssapi-devel
BuildRequires:	libicu-devel >= 2.4
BuildRequires:	libstdc++-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	mozldap-devel >= 6.0
BuildRequires:	ncurses-devel
BuildRequires:	net-snmp-devel >= 5.2.1
BuildRequires:	nspr-devel >= 1:4.4.1
BuildRequires:	nss-devel >= 1:3.9.3
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	which
BuildRequires:	zip
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
# dirty hack, maybe fedora-adminserver needed
mkdir -p __admserv/admin
touch __admserv/setup.inf

%build
%{__make} buildDirectory \
	ARCH_DEBUG="%{rpmcflags}" \
	ARCH_OPT="%{rpmcflags}" \
	BUILD_DEBUG=%{?debug:full}%{!?debug:optimize} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	MAKE=%{__make} \
	NSOS_TEST=PLD \
	ADMINUTIL_INCPATH=%{_includedir}/adminutil-1.0 \
	ADMINUTIL_LINK=-ladminutil \
	ADMINSERVER_SUBCOMPS=setup.inf \
	ADMSERV_DIR=$PWD/__admserv \
	CURSES="-lncurses" \
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
	SETUPUTIL_INCDIR=/usr/include/fedora-setuputil \
	SETUPUTIL_BINPATH=%{_bindir} \
	SVRCORE_INCLUDE="-I/usr/include/svrcore" \
	MFLAGS="\
		USE_ADMINSERVER=1 \
		USE_CONSOLE=0 \
		USE_DSMLGW=0 \
		USE_ORGCHART=1 \
		USE_DSGW=1 \
		USE_JAVATOOLS=0 \
		USE_SETUPUTIL=1 \
		USE_PERL_FROM_PATH=1 \
		DEBUG=%{?debug:full}%{!?debug:optimize} \
		NOJAVA=1"

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%files
#%defattr(644,root,root,755)
