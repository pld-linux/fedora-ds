#
# http://directory.fedora.redhat.com/wiki/Building

%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	Fedora Directory Server
Summary(pl):	-
Name:		fedora-ds
Version:	1.0.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	d8bd5b68087229b4bb2e3867cb92ba85
#Source1:	-
####%% Source1-md5:	-
Patch0:		%{name}-make.patch
URL:		http://directory.fedora.redhat.com/
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
BuildRequires:	db-devel >= 4.0
#BuildRequires:	krb-devel
BuildRequires:	libtermcap-devel
BuildRequires:	ncurses-devel
#BuildRequires:	java
#BuildRequires:	ant >= 1.6.1
#BuildRequires:	httpd-devel
BuildRequires:	apr-devel
#BuildRequires:
#BuildRequires:
#BuildRequires:
#BuildRequires:
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
Requires:	libicu >= 2.4
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
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

%package subpackage
Summary:	-
Summary(pl):	-
Group:		-

%description subpackage

%description subpackage -l pl

%package libs
Summary:	-
Summary(pl):	-
Group:		Libraries

%description libs

%description libs -l pl


%package devel
Summary:	Header files for ... library
Summary(pl):	Pliki nag³ówkowe biblioteki ...
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for ... library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl
Statyczna biblioteka ....

%prep
%setup -q
%patch0 -p1

%build
#%%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}

#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

#%{_examplesdir}/%{name}-%{version}

%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
